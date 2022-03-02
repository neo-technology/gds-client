from typing import Any

from ..graph.graph_object import Graph
from ..query_runner.query_runner import Row
from .model import Model


class NCModel(Model):
    def _query_prefix(self) -> str:
        return "CALL gds.alpha.ml.pipeline.nodeClassification.predict."

    def predict_write(self, G: Graph, **config: Any) -> Row:
        query = f"{self._query_prefix()}write($graph_name, $config)"
        config["modelName"] = self.name()
        params = {"graph_name": G.name(), "config": config}

        return self._query_runner.run_query(query, params)[0]

    def predict_write_estimate(self, G: Graph, **config: Any) -> Row:
        return self._estimate_predict("write", G.name(), config)
