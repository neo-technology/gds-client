import os
from typing import Generator

import pytest
from neo4j import GraphDatabase

from gdsclient import Neo4jQueryRunner
from gdsclient.graph_data_science import GraphDataScience

URI = os.environ.get("NEO4J_URI", "bolt://localhost:7687")

AUTH = None
if os.environ.get("NEO4J_USER") is not None:
    AUTH = (
        os.environ.get("NEO4J_USER"),
        os.environ.get("NEO4J_PASSWORD", "neo4j"),
    )


def pytest_addoption(parser):
    parser.addoption(
        "--include-enterprise", action="store_true", help="include enterprise tests"
    )


@pytest.fixture
def skip_if_not_enterprise(request) -> None:
    if not request.config.getoption("--include-enterprise"):
        pytest.skip()


def enterprise(func):
    def wrapper(skip_if_not_enterprise):
        return func

    return wrapper


@pytest.fixture(scope="package")
def runner() -> Generator[Neo4jQueryRunner, None, None]:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    runner = Neo4jQueryRunner(driver)

    yield runner

    driver.close()


@pytest.fixture(scope="package")
def gds(runner: Neo4jQueryRunner) -> GraphDataScience:
    return GraphDataScience(runner)
