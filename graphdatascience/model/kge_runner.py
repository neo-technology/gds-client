import json
import logging
import os
import time
from typing import Any, Dict, Optional

import pyarrow
import requests
from pandas import DataFrame, Series

from ..error.client_only_endpoint import client_only_endpoint
from ..error.illegal_attr_checker import IllegalAttrChecker
from ..error.uncallable_namespace import UncallableNamespace
from ..graph.graph_object import Graph
from ..query_runner.query_runner import QueryRunner
from ..server_version.server_version import ServerVersion

logging.basicConfig(level=logging.INFO)


class KgeRunner(UncallableNamespace, IllegalAttrChecker):
    def __init__(
        self,
        query_runner: QueryRunner,
        namespace: str,
        server_version: ServerVersion,
        compute_cluster_ip: str,
        encrypted_db_password: str,
        arrow_uri: str,
    ):
        self._query_runner = query_runner
        self._namespace = namespace
        self._server_version = server_version
        self._compute_cluster_web_uri = f"http://{compute_cluster_ip}:5005"
        self._compute_cluster_arrow_uri = f"grpc://{compute_cluster_ip}:8815"
        self._compute_cluster_mlflow_uri = f"http://{compute_cluster_ip}:8080"
        self._encrypted_db_password = encrypted_db_password
        self._arrow_uri = arrow_uri

    @property
    def model(self) -> "KgeRunner":
        return self

    # @compatible_with("stream", min_inclusive=ServerVersion(2, 5, 0))
    @client_only_endpoint("gds.kge.model")
    def train(
        self,
        G: Graph,
        model_name: str,
        *,
        num_epochs: int,
        embedding_dimension: int,
        epochs_per_checkpoint: Optional[int] = None,
        load_from_checkpoint: Optional[tuple[str, int]] = None,
        split_ratios=None,
        scoring_function: str = "transe",
        p_norm: float = 1.0,
        batch_size: int = 512,
        test_batch_size: int = 512,
        optimizer: str = "adam",
        optimizer_kwargs=None,
        lr_scheduler: str = "ConstantLR",
        lr_scheduler_kwargs=None,
        loss_function: str = "MarginRanking",
        loss_function_kwargs=None,
        negative_sampling_size: int = 1,
        use_node_type_aware_sampler: bool = False,
        k_value: int = 10,
        do_validation: bool = True,
        do_test: bool = True,
        filtered_metrics: bool = False,
        epochs_per_val: int = 0,
        inner_norm: bool = True,
        random_seed: Optional[int] = None,
        init_bound: Optional[float] = None,
        mlflow_experiment_name: Optional[str] = None,
    ) -> Series:
        if epochs_per_checkpoint is None:
            epochs_per_checkpoint = max(int(num_epochs / 10), 1)
        if loss_function_kwargs is None:
            loss_function_kwargs = dict(margin=1.0, adversarial_temperature=1.0, gamma=20.0)
        if lr_scheduler_kwargs is None:
            lr_scheduler_kwargs = dict(factor=1, total_iters=1000)
        if optimizer_kwargs is None:
            optimizer_kwargs = {"lr": 0.01, "weight_decay": 0.0005}
        if split_ratios is None:
            split_ratios = {"TRAIN": 0.8, "TEST": 0.2}

        algo_config = {
            key: value
            for key, value in locals().items()
            if (key not in ["self", "G", "mlflow_experiment_name", "model_name"]) and (value is not None)
        }
        print(algo_config)

        graph_config = {"name": G.name(), "config_type": "GdsGraphConfig"}

        config = {
            "user_name": "DUMMY_USER",
            "task": "KGE_TRAINING_PYG",
            "task_config": {
                "graph_config": graph_config,
                "modelname": model_name,
                "task_config": algo_config,
            },
            "graph_arrow_uri": self._arrow_uri,
        }
        if self._encrypted_db_password is not None:
            config["encrypted_db_password"] = self._encrypted_db_password

        if mlflow_experiment_name is not None:
            config["task_config"]["mlflow"] = {
                "tracking_uri": self._compute_cluster_mlflow_uri,
                "experiment_name": mlflow_experiment_name,
            }

        job_id = self._start_job(config)

        self._wait_for_job(job_id)

        return Series(
            {
                "status": "finished",
                "metrics": self._get_metrics(config["user_name"], config["task_config"]["modelname"], job_id),
            }
        )

    @client_only_endpoint("gds.kge.model")
    def predict(
        self,
        model_name: str,
        top_k: int,
        node_ids: list[int],
        rel_types: list[str],
        mlflow_experiment_name: Optional[str] = None,
    ) -> DataFrame:

        algo_config = {
            "top_k": top_k,
            "node_ids": node_ids,
            "rel_types": rel_types,
        }

        config = {
            "user_name": "DUMMY_USER",
            "task": "KGE_PREDICT_PYG",
            "task_config": {
                "graph_config": {"config_type": "GdsGraphConfig", "name": "NOGRAPH"},
                "modelname": model_name,
                "task_config": algo_config,
                "stream_rel_results": True,
            },
            "graph_arrow_uri": self._arrow_uri,
        }
        if self._encrypted_db_password is not None:
            config["encrypted_db_password"] = self._encrypted_db_password

        if mlflow_experiment_name is not None:
            config["task_config"]["mlflow"] = {
                "tracking_uri": self._compute_cluster_mlflow_uri,
                "experiment_name": mlflow_experiment_name,
            }

        job_id = self._start_job(config)

        self._wait_for_job(job_id)

        return self._stream_results(config, job_id)

    @client_only_endpoint("gds.kge.model")
    def score_triplets(
        self,
        model_name: str,
        triplets: list[tuple[int, str, int]],
        mlflow_experiment_name: Optional[str] = None,
    ) -> DataFrame:

        algo_config = {
            "triplets": triplets,
        }

        config = {
            "user_name": "DUMMY_USER",
            "task": "KGE_SCORE_TRIPLETS_PYG",
            "task_config": {
                "graph_config": {"config_type": "GdsGraphConfig", "name": "NOGRAPH"},
                "modelname": model_name,
                "task_config": algo_config,
                "stream_rel_results": True,
            },
            "graph_arrow_uri": self._arrow_uri,
        }
        if self._encrypted_db_password is not None:
            config["encrypted_db_password"] = self._encrypted_db_password

        if mlflow_experiment_name is not None:
            config["task_config"]["mlflow"] = {
                "tracking_uri": self._compute_cluster_mlflow_uri,
                "experiment_name": mlflow_experiment_name,
            }

        job_id = self._start_job(config)

        self._wait_for_job(job_id)

        return self._stream_results(config, job_id)

    def _stream_results(self, config: dict, job_id: str) -> DataFrame:
        client = pyarrow.flight.connect(self._compute_cluster_arrow_uri)

        if config["task_config"].get("stream_rel_results", False):
            upload_descriptor = pyarrow.flight.FlightDescriptor.for_path(f"{job_id}.relationships")
        else:
            raise ValueError("No results to fetch: need to set stream_rel_results or stream_graph_results to True")
        flight = client.get_flight_info(upload_descriptor)
        reader = client.do_get(flight.endpoints[0].ticket)
        read_table = reader.read_all()

        return read_table.to_pandas()

    def _get_metrics(self, user_name: str, model_name: str, job_id: str) -> DataFrame:
        res = requests.get(
            f"{self._compute_cluster_web_uri}/internal/fetch-model-metadata",
            params={"user_name": user_name, "modelname": model_name},
        )
        res.raise_for_status()

        res_file_name = f"metadata_{job_id}.json"

        with open(res_file_name, mode="wb+") as f:
            f.write(res.content)

        with open(res_file_name, mode="r") as f:
            metadata = json.load(f)

        os.remove(res_file_name)

        return metadata.get("metrics", None)

    def _start_job(self, config: Dict[str, Any]) -> str:
        url = f"{self._compute_cluster_web_uri}/api/machine-learning/start"
        res = requests.post(url, json=config)
        res.raise_for_status()
        job_id = res.json()["job_id"]
        logging.info(f"Job '{config['task']}' with ID '{job_id}' started")

        return job_id

    def _wait_for_job(self, job_id: str) -> None:
        while True:
            time.sleep(1)

            res = requests.get(f"{self._compute_cluster_web_uri}/api/machine-learning/status/{job_id}")

            res_json = res.json()
            if res_json["job_status"] == "exited":
                logging.info(f"Job with ID '{job_id}' completed")
                return
            elif res_json["job_status"] == "failed":
                error = f"KGE job failed with errors:{os.linesep}{os.linesep.join(res_json['errors'])}"
                if res.status_code == 400:
                    raise ValueError(error)
                else:
                    raise RuntimeError(error)
