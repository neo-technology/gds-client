from pandas import DataFrame

from graphdatascience import ServerVersion
from graphdatascience.call_parameters import CallParameters
from graphdatascience.query_runner.session_query_runner import SessionQueryRunner
from graphdatascience.tests.unit.conftest import CollectingQueryRunner


class FakeArrowClient:
    def connection_info(self) -> tuple[str, str]:
        return "myHost", "1234"

    def request_token(self) -> str:
        return "myToken"


def test_extracts_parameters_projection_v1() -> None:
    version = ServerVersion(2, 7, 0)
    db_query_runner = CollectingQueryRunner(version, result_mock=DataFrame([{"version": "v1"}]))
    gds_query_runner = CollectingQueryRunner(version)
    gds_query_runner.set__mock_result(DataFrame([{"databaseLocation": "remote"}]))
    qr = SessionQueryRunner.create(gds_query_runner, db_query_runner, FakeArrowClient(), True)  # type: ignore

    qr.call_procedure(
        endpoint="gds.arrow.project",
        params=CallParameters(
            graph_name="g",
            query="RETURN 1",
            concurrency=2,
            undirected_relationship_types=[],
            inverse_indexed_relationship_types=[],
            arrow_configuration={"batchSize": 100},
        ),
    )

    # doesn't run anything on GDS
    assert gds_query_runner.last_query() == ""
    assert gds_query_runner.last_params() == {}
    assert (
        db_query_runner.last_query()
        == "CALL gds.arrow.project($graph_name, $query, $concurrency, \
$undirected_relationship_types, $inverse_indexed_relationship_types, $arrow_configuration)"
    )
    assert db_query_runner.last_params() == {
        "graph_name": "g",
        "query": "RETURN 1",
        "concurrency": 2,
        "undirected_relationship_types": [],
        "inverse_indexed_relationship_types": [],
        "arrow_configuration": {
            "encrypted": False,
            "host": "myHost",
            "port": "1234",
            "token": "myToken",
            "batchSize": 100,
        },
    }


def test_extracts_parameters_projection_v2() -> None:
    version = ServerVersion(2, 7, 0)
    db_query_runner = CollectingQueryRunner(version, result_mock=DataFrame([{"version": "v1"}, {"version": "v2"}]))
    gds_query_runner = CollectingQueryRunner(version)
    gds_query_runner.set__mock_result(DataFrame([{"databaseLocation": "remote"}]))
    qr = SessionQueryRunner.create(
        gds_query_runner,
        db_query_runner,
        FakeArrowClient(),  # type: ignore
        True,
    )

    qr.call_procedure(
        endpoint="gds.arrow.project",
        params=CallParameters(
            graph_name="g",
            query="RETURN 1",
            concurrency=2,
            undirected_relationship_types=["FOO"],
            inverse_indexed_relationship_types=[],
            arrow_configuration={"batchSize": 100},
        ),
    )

    # doesn't run anything on GDS
    assert gds_query_runner.last_query() == ""
    assert gds_query_runner.last_params() == {}
    assert (
        db_query_runner.last_query()
        == "CALL gds.arrow.project.v2($graph_name, $query, $arrow_configuration, $configuration)"
    )
    assert db_query_runner.last_params() == {
        "graph_name": "g",
        "query": "RETURN 1",
        "arrow_configuration": {
            "encrypted": False,
            "host": "myHost",
            "port": "1234",
            "token": "myToken",
            "batchSize": 100,
        },
        "configuration": {
            "concurrency": 2,
            "inverseIndexedRelationshipTypes": [],
            "undirectedRelationshipTypes": ["FOO"],
        },
    }


def test_extracts_parameters_algo_write_v1() -> None:
    version = ServerVersion(2, 7, 0)
    db_query_runner = CollectingQueryRunner(version, result_mock=DataFrame([{"version": "v1"}]))
    gds_query_runner = CollectingQueryRunner(version)
    gds_query_runner.set__mock_result(DataFrame([{"databaseLocation": "remote"}]))
    qr = SessionQueryRunner.create(gds_query_runner, db_query_runner, FakeArrowClient(), True)  # type: ignore

    qr.call_procedure(endpoint="gds.degree.write", params=CallParameters(graph_name="g", config={"jobId": "my-job"}))

    assert gds_query_runner.last_query() == "CALL gds.degree.write($graph_name, $config)"
    assert gds_query_runner.last_params() == {
        "graph_name": "g",
        "config": {"jobId": "my-job", "writeToResultStore": True},
    }
    assert (
        db_query_runner.last_query() == "CALL gds.arrow.write($graphName, $databaseName, $jobId, $arrowConfiguration)"
    )
    assert db_query_runner.last_params() == {
        "graphName": "g",
        "databaseName": "dummy",
        "jobId": "my-job",
        "arrowConfiguration": {"encrypted": False, "host": "myHost", "port": "1234", "token": "myToken"},
    }


def test_extracts_parameters_algo_write_v2() -> None:
    version = ServerVersion(2, 7, 0)
    db_query_runner = CollectingQueryRunner(version, result_mock=DataFrame([{"version": "v1"}, {"version": "v2"}]))
    gds_query_runner = CollectingQueryRunner(version)
    gds_query_runner.set__mock_result(DataFrame([{"databaseLocation": "remote"}]))
    qr = SessionQueryRunner.create(
        gds_query_runner,
        db_query_runner,
        FakeArrowClient(),  # type: ignore
        True,
    )

    qr.call_procedure(
        endpoint="gds.degree.write", params=CallParameters(graph_name="g", config={"jobId": "my-job", "concurrency": 2})
    )

    assert gds_query_runner.last_query() == "CALL gds.degree.write($graph_name, $config)"
    assert gds_query_runner.last_params() == {
        "graph_name": "g",
        "config": {"jobId": "my-job", "writeToResultStore": True, "concurrency": 2},
    }
    assert (
        db_query_runner.last_query()
        == "CALL gds.arrow.write.v2($graphName, $jobId, $arrowConfiguration, $configuration)"
    )
    assert db_query_runner.last_params() == {
        "graphName": "g",
        "jobId": "my-job",
        "arrowConfiguration": {"encrypted": False, "host": "myHost", "port": "1234", "token": "myToken"},
        "configuration": {"concurrency": 2},
    }


def test_arrow_and_write_configuration() -> None:
    version = ServerVersion(2, 7, 0)
    db_query_runner = CollectingQueryRunner(version, result_mock=DataFrame([{"version": "v1"}]))
    gds_query_runner = CollectingQueryRunner(version)
    gds_query_runner.set__mock_result(DataFrame([{"databaseLocation": "remote"}]))
    qr = SessionQueryRunner.create(gds_query_runner, db_query_runner, FakeArrowClient(), True)  # type: ignore

    qr.call_procedure(
        endpoint="gds.degree.write",
        params=CallParameters(
            graph_name="g",
            config={"arrowConfiguration": {"batchSize": 1000}, "jobId": "my-job"},
        ),
    )

    assert gds_query_runner.last_query() == "CALL gds.degree.write($graph_name, $config)"
    assert gds_query_runner.last_params() == {
        "graph_name": "g",
        "config": {"writeToResultStore": True, "jobId": "my-job"},
    }
    assert (
        db_query_runner.last_query() == "CALL gds.arrow.write($graphName, $databaseName, $jobId, $arrowConfiguration)"
    )
    assert db_query_runner.last_params() == {
        "graphName": "g",
        "databaseName": "dummy",
        "jobId": "my-job",
        "arrowConfiguration": {
            "encrypted": False,
            "host": "myHost",
            "port": "1234",
            "token": "myToken",
            "batchSize": 1000,
        },
    }


def test_arrow_and_write_configuration_graph_write() -> None:
    version = ServerVersion(2, 7, 0)
    db_query_runner = CollectingQueryRunner(version, result_mock=DataFrame([{"version": "v1"}]))
    gds_query_runner = CollectingQueryRunner(version)
    gds_query_runner.set__mock_result(DataFrame([{"databaseLocation": "remote"}]))
    qr = SessionQueryRunner.create(gds_query_runner, db_query_runner, FakeArrowClient(), True)  # type: ignore

    qr.call_procedure(
        endpoint="gds.graph.nodeProperties.write",
        params=CallParameters(
            graph_name="g",
            properties=[],
            entities=[],
            config={"arrowConfiguration": {"batchSize": 42}, "jobId": "my-job"},
        ),
    )

    assert (
        gds_query_runner.last_query()
        == "CALL gds.graph.nodeProperties.write($graph_name, $properties, $entities, $config)"
    )
    assert gds_query_runner.last_params() == {
        "graph_name": "g",
        "entities": [],
        "properties": [],
        "config": {"writeToResultStore": True, "jobId": "my-job"},
    }
    assert (
        db_query_runner.last_query() == "CALL gds.arrow.write($graphName, $databaseName, $jobId, $arrowConfiguration)"
    )
    assert db_query_runner.last_params() == {
        "graphName": "g",
        "databaseName": "dummy",
        "jobId": "my-job",
        "arrowConfiguration": {
            "encrypted": False,
            "host": "myHost",
            "port": "1234",
            "token": "myToken",
            "batchSize": 42,
        },
    }
