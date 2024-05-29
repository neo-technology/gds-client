..
    DO NOT EDIT - File generated automatically

Algorithms procedures
----------------------
Listing of all algorithm procedures in the Neo4j Graph Data Science Python Client API.
These all assume that an object of :class:`.GraphDataScience` is available as `gds`.

.. py:function:: gds.allShortestPaths.delta.mutate(G: Graph, **config: Any) -> Series[Any]

    The Delta Stepping shortest path algorithm computes the shortest (weighted) path
    between one node and any other node in the graph. The computation is run multi-threaded.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.allShortestPaths.delta.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for allShortestPaths.dealta.mutate.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.allShortestPaths.delta.stats(G: Graph, **config: Any) -> Series[Any]

    The Delta Stepping shortest path algorithm computes the shortest (weighted) path
    between one node and any other node in the graph. The computation is run multi-threaded

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.allShortestPaths.delta.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for allShortestPaths.delta.stats.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.allShortestPaths.delta.stream(G: Graph, **config: Any) -> DataFrame

    The Delta Stepping shortest path algorithm computes the shortest (weighted) path
    between one node and any other node in the graph. The computation is run multi-threaded.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.allShortestPaths.delta.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for allShortestPaths.delta.strema.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.allShortestPaths.delta.write(G: Graph, **config: Any) -> Series[Any]

    The Delta Stepping shortest path algorithm computes the shortest (weighted) path
    between one node and any other node in the graph. The computation is run multi-threaded.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.allShortestPaths.delta.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.allShortestPaths.dijkstra.mutate(G: Graph, **config: Any) -> Series[Any]

    The Dijkstra shortest path algorithm computes the shortest (weighted) path
    between one node and any other node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.allShortestPaths.dijkstra.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.allShortestPaths.dijkstra.stream(G: Graph, **config: Any) -> DataFrame

    The Dijkstra shortest path algorithm computes the shortest (weighted) path
    between one node and any other node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.allShortestPaths.dijkstra.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.allShortestPaths.dijkstra.write(G: Graph, **config: Any) -> Series[Any]

    The Dijkstra shortest path algorithm computes the shortest (weighted) path
    between one node and any other node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.allShortestPaths.dijkstra.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.allShortestPaths.stream(G: Graph, **config: Any) -> DataFrame

    The All Pairs Shortest Path (APSP) calculates the shortest (weighted) path
    between all pairs of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.allShortestPaths.stream(G: Graph, **config: Any) -> DataFrame

    The All Pairs Shortest Path (APSP) calculates the shortest (weighted) path
    between all pairs of nodes.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.allShortestPaths.stream` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.closeness.harmonic.stream(G: Graph, **config: Any) -> DataFrame

    Harmonic centrality is a way of detecting nodes that are able to spread information
    very efficiently through a graph.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.closeness.harmonic.stream` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.closeness.harmonic.write(G: Graph, **config: Any) -> Series[Any]

    Harmonic centrality is a way of detecting nodes that are able to spread information
    very efficiently through a graph.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.closeness.harmonic.write` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.conductance.stream(G: Graph, **config: Any) -> DataFrame

    Evaluates a division of nodes into communities based on the proportion of relationships
    that cross community boundaries.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.graph.sample.rwr(graph_name: str, from_G: Graph, **config: Any) -> GraphCreateResult

    Constructs a random subgraph based on random walks with restarts.

.. deprecated:: 2.4.0
   Since GDS server version 2.4.0 you should use the endpoint :func:`gds.graph.sample.rwr` instead.

    |

    **Parameters:**

        * **graph_name** - str

        * **from_G** - Graph

.. py:function:: gds.alpha.hits.mutate(G: Graph, **config: Any) -> Series[Any]

    Hyperlink-Induced Topic Search (HITS) is a link analysis algorithm that rates nodes.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.hits.mutate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.hits.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.hits.mutate.estimate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.hits.stats(G: Graph, **config: Any) -> Series[Any]

    Hyperlink-Induced Topic Search (HITS) is a link analysis algorithm that rates nodes.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.hits.stats` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.hits.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.hits.stats.estimate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.hits.stream(G: Graph, **config: Any) -> DataFrame

    Hyperlink-Induced Topic Search (HITS) is a link analysis algorithm that rates nodes.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.hits.stream` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.hits.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.hits.stream.estimate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.hits.write(G: Graph, **config: Any) -> Series[Any]

    Hyperlink-Induced Topic Search (HITS) is a link analysis algorithm that rates nodes.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.hits.write` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.hits.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.hits.write.estimate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.kSpanningTree.write(G: Graph, **config: Any) -> Series[Any]

    The K-spanning tree algorithm starts from a root node and returns a spanning tree with exactly k nodes

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.kSpanningTree.write` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.knn.filtered.mutate(G: Graph, **config: Any) -> Series[Any]

    The k-nearest neighbor graph algorithm constructs relationships between nodes if the distance
    between two nodes is among the k nearest distances compared to other nodes.
    KNN computes distances based on the similarity of node properties.
    Filtered KNN extends this functionality, allowing filtering on source nodes and target nodes, respectively.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.knn.filtered.stats(G: Graph, **config: Any) -> Series[Any]

    The k-nearest neighbor graph algorithm constructs relationships between nodes if the distance
    between two nodes is among the k nearest distances compared to other nodes.
    KNN computes distances based on the similarity of node properties.
    Filtered KNN extends this functionality, allowing filtering on source nodes and target nodes, respectively.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.knn.filtered.stream(G: Graph, **config: Any) -> DataFrame

    The k-nearest neighbor graph algorithm constructs relationships between nodes if the distance
    between two nodes is among the k nearest distances compared to other nodes.
    KNN computes distances based on the similarity of node properties.
    Filtered KNN extends this functionality, allowing filtering on source nodes and target nodes, respectively.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.knn.filtered.write(G: Graph, **config: Any) -> Series[Any]

    The k-nearest neighbor graph algorithm constructs relationships between nodes if the distance
    between two nodes is among the k nearest distances compared to other nodes.
    KNN computes distances based on the similarity of node properties.
    Filtered KNN extends this functionality, allowing filtering on source nodes and target nodes, respectively.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.maxkcut.mutate(G: Graph, **config: Any) -> Series[Any]

    Approximate Maximum k-cut maps each node into one of k disjoint communities
    trying to maximize the sum of weights of relationships between these communities.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.maxkcut.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Approximate Maximum k-cut maps each node into one of k disjoint communities
    trying to maximize the sum of weights of relationships between these communities.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.maxkcut.stream(G: Graph, **config: Any) -> DataFrame

    Approximate Maximum k-cut maps each node into one of k disjoint communities
    trying to maximize the sum of weights of relationships between these communities.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.maxkcut.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Approximate Maximum k-cut maps each node into one of k disjoint communities
    trying to maximize the sum of weights of relationships between these communities.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.modularity.stats(G: Graph, **config: Any) -> Series[Any]

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.modularity.stream(G: Graph, **config: Any) -> DataFrame

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.nodeSimilarity.filtered.mutate(G: Graph, **config: Any) -> Series[Any]

    The Filtered Node Similarity algorithm compares a set of nodes based on the nodes they are connected to.
    Two nodes are considered similar if they share many of the same neighbors.
    The algorithm computes pair-wise similarities based on Jaccard or Overlap metrics.
    The filtered variant supports limiting which nodes to compare via source and target node filters.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.nodeSimilarity.filtered.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.nodeSimilarity.filtered.stats(G: Graph, **config: Any) -> Series[Any]

    The Filtered Node Similarity algorithm compares a set of nodes based on the nodes they are connected to.
    Two nodes are considered similar if they share many of the same neighbors.
    The algorithm computes pair-wise similarities based on Jaccard or Overlap metrics.
    The filtered variant supports limiting which nodes to compare via source and target node filters.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.nodeSimilarity.filtered.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.nodeSimilarity.filtered.stream(G: Graph, **config: Any) -> DataFrame

    The Filtered Node Similarity algorithm compares a set of nodes based on the nodes they are connected to.
    Two nodes are considered similar if they share many of the same neighbors.
    The algorithm computes pair-wise similarities based on Jaccard or Overlap metrics.
    The filtered variant supports limiting which nodes to compare via source and target node filters.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.nodeSimilarity.filtered.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.nodeSimilarity.filtered.write(G: Graph, **config: Any) -> Series[Any]

    The Filtered Node Similarity algorithm compares a set of nodes based on the nodes they are connected to.
    Two nodes are considered similar if they share many of the same neighbors.
    The algorithm computes pair-wise similarities based on Jaccard or Overlap metrics.
    The filtered variant supports limiting which nodes to compare via source and target node filters.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.nodeSimilarity.filtered.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.scaleProperties.mutate(G: Graph, **config: Any) -> Series[Any]

    Scale node properties

.. deprecated:: 2.4.0
   Since GDS server version 2.4.0 you should use the endpoint :func:`gds.scaleProperties.mutate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.scaleProperties.stream(G: Graph, **config: Any) -> DataFrame

    Scale node properties

.. deprecated:: 2.4.0
   Since GDS server version 2.4.0 you should use the endpoint :func:`gds.scaleProperties.stream` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.scc.stream(G: Graph, **config: Any) -> DataFrame

    The SCC algorithm finds sets of connected nodes in an directed graph,
    where all nodes in the same set form a connected component.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.scc.write(G: Graph, **config: Any) -> Series[Any]

    The SCC algorithm finds sets of connected nodes in an directed graph,
    where all nodes in the same set form a connected component.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.sllpa.mutate(G: Graph, **config: Any) -> Series[Any]

    The Speaker Listener Label Propagation algorithm is a fast algorithm for finding overlapping communities in a graph.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.sllpa.mutate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.sllpa.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.sllpa.mutate.estimate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.sllpa.stats(G: Graph, **config: Any) -> Series[Any]

    The Speaker Listener Label Propagation algorithm is a fast algorithm for finding overlapping communities in a graph.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.sllpa.stats` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.sllpa.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.sllpa.stats.estimate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.sllpa.stream(G: Graph, **config: Any) -> DataFrame

    The Speaker Listener Label Propagation algorithm is a fast algorithm for finding overlapping communities in a graph.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.sllpa.stream` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.sllpa.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.sllpa.stream.estimate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.sllpa.write(G: Graph, **config: Any) -> Series[Any]

    The Speaker Listener Label Propagation algorithm is a fast algorithm for finding overlapping communities in a graph.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.sllpa.write` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.sllpa.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.sllpa.write.estimate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.triangles(G: Graph, **config: Any) -> DataFrame

    Triangles streams the nodeIds of each triangle in the graph.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.triangles` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.articleRank.mutate(G: Graph, **config: Any) -> Series[Any]

    Article Rank is a variant of the Page Rank algorithm, which measures the transitive influence or connectivity of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.articleRank.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.articleRank.stats(G: Graph, **config: Any) -> Series[Any]

    Executes the algorithm and returns result statistics without writing the result to Neo4j.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.articleRank.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: scaler(G: Graph, *, , dampingFactor='0.85', maxIterations='20', tolerance='0.0000001', relationshipWeightProperty='None', sourceNodes='[]', scaler='None': Any) -> DataFrame

    Article Rank is a variant of the Page Rank algorithm, which measures the transitive influence or connectivity of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.articleRank.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.articleRank.write(G: Graph, **config: Any) -> Series[Any]

    Article Rank is a variant of the Page Rank algorithm, which measures the transitive influence or connectivity of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.articleRank.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.bellmanFord.mutate(G: Graph, **config: Any) -> Series[Any]

    The Bellman-Ford shortest path algorithm computes the shortest (weighted) path between one node
    and any other node in the graph without negative cycles.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.bellmanFord.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.bellmanFord.stats(G: Graph, **config: Any) -> Series[Any]

    The Bellman-Ford shortest path algorithm computes the shortest (weighted) path between one node
    and any other node in the graph without negative cycles.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.bellmanFord.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.bellmanFord.stream(G: Graph, **config: Any) -> DataFrame

    The Bellman-Ford shortest path algorithm computes the shortest (weighted) path between one node
    and any other node in the graph without negative cycles.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.bellmanFord.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.bellmanFord.write(G: Graph, **config: Any) -> Series[Any]

    The Bellman-Ford shortest path algorithm computes the shortest (weighted) path between one node
    and any other node in the graph without negative cycles.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.bellmanFord.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.closeness.mutate(G: Graph, **config: Any) -> Series[Any]

    Closeness centrality is a way of detecting nodes that are able to spread information very efficiently through a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.closeness.stats(G: Graph, **config: Any) -> Series[Any]

    Closeness centrality is a way of detecting nodes that are able to spread information very efficiently through a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.closeness.stream(G: Graph, **config: Any) -> DataFrame

    Closeness centrality is a way of detecting nodes that are able to spread information very efficiently through a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.closeness.write(G: Graph, **config: Any) -> Series[Any]

    Closeness centrality is a way of detecting nodes that are able to spread information very efficiently through a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.collapsePath.mutate(G: Graph, **config: Any) -> Series[Any]

    Collapse Path algorithm is a traversal algorithm capable of creating relationships between the start
    and end nodes of a traversal

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.influenceMaximization.celf.mutate(G: Graph, **config: Any) -> Series[Any]

    The Cost Effective Lazy Forward (CELF) algorithm aims to find k nodes
    that maximize the expected spread of influence in the network.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.influenceMaximization.celf.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.influenceMaximization.celf.stats(G: Graph, **config: Any) -> Series[Any]

    Executes the algorithm and returns result statistics without writing the result to Neo4j.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.influenceMaximization.celf.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.influenceMaximization.celf.stream(G: Graph, **config: Any) -> DataFrame

    The Cost Effective Lazy Forward (CELF) algorithm aims to find k nodes
    that maximize the expected spread of influence in the network.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.influenceMaximization.celf.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    The Cost Effective Lazy Forward (CELF) algorithm aims to find k nodes
    that maximize the expected spread of influence in the network.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.influenceMaximization.celf.write(G: Graph, **config: Any) -> Series[Any]

    The Cost Effective Lazy Forward (CELF) algorithm aims to find k nodes
    that maximize the expected spread of influence in the network.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.influenceMaximization.celf.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.k1coloring.mutate(G: Graph, **config: Any) -> Series[Any]

    The K-1 Coloring algorithm assigns a color to every node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.k1coloring.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.k1coloring.stats(G: Graph, **config: Any) -> Series[Any]

    The K-1 Coloring algorithm assigns a color to every node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.k1coloring.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.k1coloring.stream(G: Graph, **config: Any) -> DataFrame

    The K-1 Coloring algorithm assigns a color to every node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.k1coloring.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.k1coloring.write(G: Graph, **config: Any) -> Series[Any]

    The K-1 Coloring algorithm assigns a color to every node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.k1coloring.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.kmeans.mutate(G: Graph, **config: Any) -> Series[Any]

    The Kmeans  algorithm clusters nodes into different communities based on Euclidean distance

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.kmeans.mutate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.kmeans.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.kmeans.mutate.estimate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.kmeans.stats(G: Graph, **config: Any) -> Series[Any]

    The Kmeans  algorithm clusters nodes into different communities based on Euclidean distance

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.kmeans.stats` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.kmeans.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.kmeans.stats.estimate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.kmeans.stream(G: Graph, **config: Any) -> DataFrame

    The Kmeans  algorithm clusters nodes into different communities based on Euclidean distance

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.kmeans.stream` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.kmeans.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.kmeans.stream.estimate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.kmeans.write(G: Graph, **config: Any) -> Series[Any]

    The Kmeans  algorithm clusters nodes into different communities based on Euclidean distance

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.kmeans.write` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.kmeans.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

.. deprecated:: 2.5.0
   Since GDS server version 2.5.0 you should use the endpoint :func:`gds.kmeans.write.estimate` instead.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.leiden.mutate(G: Graph, **config: Any) -> Series[Any]

    Leiden is a community detection algorithm, which guarantees that communities are well connected

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.leiden.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.leiden.stats(G: Graph, **config: Any) -> Series[Any]

    Executes the algorithm and returns result statistics without writing the result to Neo4j.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.leiden.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.leiden.stream(G: Graph, **config: Any) -> DataFrame

    Leiden is a community detection algorithm, which guarantees that communities are well connected

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.leiden.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.leiden.write(G: Graph, **config: Any) -> Series[Any]

    Leiden is a community detection algorithm, which guarantees that communities are well connected

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.leiden.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.modularityOptimization.mutate(G: Graph, **config: Any) -> Series[Any]

    The Modularity Optimization algorithm groups the nodes in the graph by optimizing the graphs modularity.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.modularityOptimization.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.modularityOptimization.stream(G: Graph, **config: Any) -> DataFrame

    The Modularity Optimization algorithm groups the nodes in the graph by optimizing the graphs modularity.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.modularityOptimization.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.modularityOptimization.write(G: Graph, **config: Any) -> Series[Any]

    The Modularity Optimization algorithm groups the nodes in the graph by optimizing the graphs modularity.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.modularityOptimization.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scaleProperties.mutate(G: Graph, **config: Any) -> Series[Any]

    Scale node properties

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scaleProperties.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scaleProperties.stats(G: Graph, **config: Any) -> Series[Any]

    Scale node properties

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scaleProperties.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scaleProperties.stream(G: Graph, **config: Any) -> DataFrame

    Scale node properties

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scaleProperties.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scaleProperties.write(G: Graph, **config: Any) -> Series[Any]

    Scale node properties

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scaleProperties.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scc.mutate(G: Graph, **config: Any) -> Series[Any]

    The SCC algorithm finds sets of connected nodes in an directed graph, where all nodes in the same set form a connected component.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scc.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for SCC.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scc.stats(G: Graph, **config: Any) -> Series[Any]

    The SCC algorithm finds sets of connected nodes in an directed graph, where all nodes in the same set form a connected component.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scc.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for SCC.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scc.stream(G: Graph, **config: Any) -> DataFrame

    The SCC algorithm finds sets of connected nodes in an directed graph, where all nodes in the same set form a connected component.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scc.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for SCC.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scc.write(G: Graph, **config: Any) -> Series[Any]

    The SCC algorithm finds sets of connected nodes in an directed graph, where all nodes in the same set form a connected component.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.scc.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for SCC.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.spanningTree.mutate(G: Graph, **config: Any) -> Series[Any]

    The spanning tree algorithm visits all nodes that are in the same connected component as the starting node,
    and returns a spanning tree of all nodes in the component where the total weight of the relationships is either minimized or maximized.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.spanningTree.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.spanningTree.stats(G: Graph, **config: Any) -> Series[Any]

    The spanning tree algorithm visits all nodes that are in the same connected component as the starting node,
    and returns a spanning tree of all nodes in the component
    where the total weight of the relationships is either minimized or maximized.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.spanningTree.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.spanningTree.stream(G: Graph, **config: Any) -> DataFrame

    The spanning tree algorithm visits all nodes that are in the same connected component as the starting node,
    and returns a spanning tree of all nodes in the component
    where the total weight of the relationships is either minimized or maximized.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.spanningTree.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.spanningTree.write(G: Graph, **config: Any) -> Series[Any]

    The spanning tree algorithm visits all nodes that are in the same connected component as the starting node,
    and returns a spanning tree of all nodes in the component
    where the total weight of the relationships is either minimized or maximized.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.spanningTree.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.steinerTree.mutate(G: Graph, **config: Any) -> Series[Any]

    The steiner tree algorithm accepts a source node, as well as a list of target nodes.
    It then attempts to find a spanning tree where there is a path from the source node to each target node,
    such that the total weight of the relationships is as low as possible.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.steinerTree.stats(G: Graph, **config: Any) -> Series[Any]

    The steiner tree algorithm accepts a source node, as well as a list of target nodes.
    It then attempts to find a spanning tree where there is a path from the source node to each target node,
    such that the total weight of the relationships is as low as possible.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.steinerTree.stream(G: Graph, **config: Any) -> DataFrame

    The steiner tree algorithm accepts a source node, as well as a list of target nodes.
    It then attempts to find a spanning tree where there is a path from the source node to each target node,
    such that the total weight of the relationships is as low as possible.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.beta.steinerTree.write(G: Graph, **config: Any) -> Series[Any]

    The steiner tree algorithm accepts a source node, as well as a list of target nodes.
    It then attempts to find a spanning tree where there is a path from the source node to each target node,
    such that the total weight of the relationships is as low as possible.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.betweenness.mutate(G: Graph, **config: Any) -> Series[Any]

    Betweenness centrality measures the relative information flow that passes through a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.betweenness.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Betweenness centrality measures the relative information flow that passes through a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.betweenness.stats(G: Graph, **config: Any) -> Series[Any]

    Betweenness centrality measures the relative information flow that passes through a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.betweenness.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Betweenness centrality measures the relative information flow that passes through a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: relationshipWeightProperty(G: Graph, *, , samplingSize='node count', samplingSeed='None', relationshipWeightProperty='None': Any) -> DataFrame

    Betweenness centrality measures the relative information flow that passes through a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.betweenness.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Betweenness centrality measures the relative information flow that passes through a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.betweenness.write(G: Graph, **config: Any) -> Series[Any]

    Betweenness centrality measures the relative information flow that passes through a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.betweenness.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Betweenness centrality measures the relative information flow that passes through a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.bfs.mutate(G: Graph, **config: Any) -> Series[Any]

    BFS is a traversal algorithm, which explores all of the neighbor nodes at the present depth
    prior to moving on to the nodes at the next depth level.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.bfs.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.bfs.stats(G: Graph, **config: Any) -> Series[Any]

    BFS is a traversal algorithm, which explores all of the neighbor nodes at the present depth
    prior to moving on to the nodes at the next depth level.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.bfs.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: maxDepth(G: Graph, *, , sourceNode, targetNodes='empty list', maxDepth='-1': Any) -> DataFrame

    BFS is a traversal algorithm, which explores all of the neighbor nodes at the present depth
    prior to moving on to the nodes at the next depth level.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.bfs.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    BFS is a traversal algorithm, which explores all of the neighbor nodes at the present depth
    prior to moving on to the nodes at the next depth level.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.closeness.mutate(G: Graph, **config: Any) -> Series[Any]

    Closeness centrality is a way of detecting nodes that are able to spread information very efficiently through a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.closeness.stats(G: Graph, **config: Any) -> Series[Any]

    Closeness centrality is a way of detecting nodes that are able to spread information very efficiently through a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.closeness.stream(G: Graph, **config: Any) -> DataFrame

    Closeness centrality is a way of detecting nodes that are able to spread information very efficiently through a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.closeness.write(G: Graph, **config: Any) -> Series[Any]

    Closeness centrality is a way of detecting nodes that are able to spread information very efficiently through a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.closeness.harmonic.mutate(G: Graph, **config: Any) -> DataFrame

    Harmonic centrality is a way of detecting nodes that are able to spread information
    very efficiently through a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.closeness.harmonic.stats(G: Graph, **config: Any) -> DataFrame

    Harmonic centrality is a way of detecting nodes that are able to spread information
    very efficiently through a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.closeness.harmonic.stream(G: Graph, **config: Any) -> DataFrame

    Harmonic centrality is a way of detecting nodes that are able to spread information
    very efficiently through a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.closeness.harmonic.write(G: Graph, **config: Any) -> Series[Any]

    Harmonic centrality is a way of detecting nodes that are able to spread information
    very efficiently through a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.collapsePath.mutate(G: Graph, **config: Any) -> Series[Any]

    Collapse Path algorithm is a traversal algorithm capable of creating relationships between the start
    and end nodes of a traversal

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: relationshipWeightProperty(G: Graph, *, , communityProperty, relationshipWeightProperty='None': Any) -> DataFrame

    Evaluates a division of nodes into communities based on the proportion of relationships
    that cross community boundaries.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.dag.topologicalSort.stream(G: Graph, **config: Any) -> DataFrame

    Returns a topological ordering of the nodes in a directed acyclic graph (DAG).

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.dag.longestPath.stream(G: Graph, **config: Any) -> DataFrame

    Finds the longest path that leads to a node in a directed acyclic graph (DAG).

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.degree.mutate(G: Graph, **config: Any) -> Series[Any]

    Degree centrality measures the number of incoming and outgoing relationships from a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.degree.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Degree centrality measures the number of incoming and outgoing relationships from a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.degree.stats(G: Graph, **config: Any) -> Series[Any]

    Degree centrality measures the number of incoming and outgoing relationships from a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.degree.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Degree centrality measures the number of incoming and outgoing relationships from a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: relationshipWeightProperty(G: Graph, *, , orientation='NATURAL', relationshipWeightProperty='None': Any) -> DataFrame

    Degree centrality measures the number of incoming and outgoing relationships from a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.degree.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Degree centrality measures the number of incoming and outgoing relationships from a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.degree.write(G: Graph, **config: Any) -> Series[Any]

    Degree centrality measures the number of incoming and outgoing relationships from a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.degree.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Degree centrality measures the number of incoming and outgoing relationships from a node.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.dfs.mutate(G: Graph, **config: Any) -> Series[Any]

    Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures.
    The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph)
    and explores as far as possible along each branch before backtracking.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.dfs.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: maxDepth(G: Graph, *, , sourceNode, targetNodes='empty list', maxDepth='-1': Any) -> DataFrame

    Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures.
    The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph)
    and explores as far as possible along each branch before backtracking.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.dfs.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures.
    The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph)
    and explores as far as possible along each branch before backtracking.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.eigenvector.mutate(G: Graph, **config: Any) -> Series[Any]

    Eigenvector Centrality is an algorithm that measures the transitive influence or connectivity of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.eigenvector.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.eigenvector.stats(G: Graph, **config: Any) -> Series[Any]

    Eigenvector Centrality is an algorithm that measures the transitive influence or connectivity of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.eigenvector.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: scaler(G: Graph, *, , maxIterations='20', tolerance='0.0000001', relationshipWeightProperty='None', sourceNodes='[]', scaler='None': Any) -> DataFrame

    Eigenvector Centrality is an algorithm that measures the transitive influence or connectivity of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.eigenvector.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.eigenvector.write(G: Graph, **config: Any) -> Series[Any]

    Eigenvector Centrality is an algorithm that measures the transitive influence or connectivity of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.eigenvector.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.graph.sample.cnarw(graph_name: str, from_G: Graph, **config: Any) -> GraphCreateResult

    Constructs a random subgraph based on common-neighbour-aware random walks.

    |

    **Parameters:**

        * **graph_name** - str

        * **from_G** - Graph

.. py:function:: gds.graph.sample.cnarw.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.graph.sample.rwr(graph_name: str, from_G: Graph, **config: Any) -> GraphCreateResult

    Constructs a random subgraph based on random walks with restarts.

    |

    **Parameters:**

        * **graph_name** - str

        * **from_G** - Graph

.. py:function:: gds.hits.mutate(G: Graph, **config: Any) -> Series[Any]

    Hyperlink-Induced Topic Search (HITS) is a link analysis algorithm that rates nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.hits.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.hits.stats(G: Graph, **config: Any) -> Series[Any]

    Hyperlink-Induced Topic Search (HITS) is a link analysis algorithm that rates nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.hits.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.hits.stream(G: Graph, **config: Any) -> DataFrame

    Hyperlink-Induced Topic Search (HITS) is a link analysis algorithm that rates nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.hits.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.hits.write(G: Graph, **config: Any) -> Series[Any]

    Hyperlink-Induced Topic Search (HITS) is a link analysis algorithm that rates nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.hits.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.influenceMaximization.celf.mutate(G: Graph, **config: Any) -> Series[Any]

    The Cost Effective Lazy Forward (CELF) algorithm aims to find k nodes
    that maximize the expected spread of influence in the network.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.influenceMaximization.celf.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.influenceMaximization.celf.stats(G: Graph, **config: Any) -> Series[Any]

    Executes the algorithm and returns result statistics without writing the result to Neo4j.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.influenceMaximization.celf.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.influenceMaximization.celf.stream(G: Graph, **config: Any) -> DataFrame

    The Cost Effective Lazy Forward (CELF) algorithm aims to find k nodes
    that maximize the expected spread of influence in the network.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.influenceMaximization.celf.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    The Cost Effective Lazy Forward (CELF) algorithm aims to find k nodes
    that maximize the expected spread of influence in the network.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.influenceMaximization.celf.write(G: Graph, **config: Any) -> Series[Any]

    The Cost Effective Lazy Forward (CELF) algorithm aims to find k nodes
    that maximize the expected spread of influence in the network.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.influenceMaximization.celf.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kmeans.mutate(G: Graph, **config: Any) -> Series[Any]

    The Kmeans  algorithm clusters nodes into different communities based on Euclidean distance

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kmeans.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kmeans.stats(G: Graph, **config: Any) -> Series[Any]

    The Kmeans  algorithm clusters nodes into different communities based on Euclidean distance

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kmeans.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kmeans.stream(G: Graph, **config: Any) -> DataFrame

    The Kmeans  algorithm clusters nodes into different communities based on Euclidean distance

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kmeans.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kmeans.write(G: Graph, **config: Any) -> Series[Any]

    The Kmeans  algorithm clusters nodes into different communities based on Euclidean distance

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kmeans.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.k1coloring.mutate(G: Graph, **config: Any) -> Series[Any]

    The K-1 Coloring algorithm assigns a color to every node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.k1coloring.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.k1coloring.stats(G: Graph, **config: Any) -> Series[Any]

    The K-1 Coloring algorithm assigns a color to every node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.k1coloring.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.k1coloring.stream(G: Graph, **config: Any) -> DataFrame

    The K-1 Coloring algorithm assigns a color to every node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.k1coloring.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.k1coloring.write(G: Graph, **config: Any) -> Series[Any]

    The K-1 Coloring algorithm assigns a color to every node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.k1coloring.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kcore.mutate(G: Graph, **config: Any) -> Series[Any]

    Computes the k-core values in a network

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kcore.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kcore.stats(G: Graph, **config: Any) -> Series[Any]

    Computes the k-core values in a network

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kcore.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kcore.stream(G: Graph, **config: Any) -> Series[Any]

    Computes the k-core values in a network

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kcore.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kcore.write(G: Graph, **config: Any) -> Series[Any]

    Computes the k-core values in a network

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kcore.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.mutate(G: Graph, **config: Any) -> Series[Any]

    The k-nearest neighbor graph algorithm constructs relationships between nodes if the distance
    between two nodes is among the k nearest distances compared to other nodes.
    KNN computes distances based on the similarity of node properties

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.stats(G: Graph, **config: Any) -> Series[Any]

    The k-nearest neighbor graph algorithm constructs relationships between nodes if the distance
    between two nodes is among the k nearest distances compared to other nodes.
    KNN computes distances based on the similarity of node properties

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.stream(G: Graph, **config: Any) -> DataFrame

    The k-nearest neighbor graph algorithm constructs relationships between nodes if the distance
    between two nodes is among the k nearest distances compared to other nodes.
    KNN computes distances based on the similarity of node properties

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.write(G: Graph, **config: Any) -> Series[Any]

    The k-nearest neighbor graph algorithm constructs relationships between nodes if the distance
    between two nodes is among the k nearest distances compared to other nodes.
    KNN computes distances based on the similarity of node properties

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.filtered.mutate(G: Graph, **config: Any) -> Series[Any]

    The k-nearest neighbor graph algorithm constructs relationships between nodes if the distance
    between two nodes is among the k nearest distances compared to other nodes.
    KNN computes distances based on the similarity of node properties.
    Filtered KNN extends this functionality, allowing filtering on source nodes and target nodes, respectively.
    
    .. py:function:: gds.knn.filtered.mutate.estimate(G: Graph, **config: Any) -> Series[Any]
    
    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.filtered.stats(G: Graph, **config: Any) -> Series[Any]

    The k-nearest neighbor graph algorithm constructs relationships between nodes if the distance
    between two nodes is among the k nearest distances compared to other nodes.
    KNN computes distances based on the similarity of node properties.
    Filtered KNN extends this functionality, allowing filtering on source nodes and target nodes, respectively.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.filtered.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.filtered.stream(G: Graph, **config: Any) -> DataFrame

    The k-nearest neighbor graph algorithm constructs relationships between nodes if the distance
    between two nodes is among the k nearest distances compared to other nodes.
    KNN computes distances based on the similarity of node properties.
    Filtered KNN extends this functionality, allowing filtering on source nodes and target nodes, respectively.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.filtered.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.filtered.write(G: Graph, **config: Any) -> Series[Any]

    The k-nearest neighbor graph algorithm constructs relationships between nodes if the distance
    between two nodes is among the k nearest distances compared to other nodes.
    KNN computes distances based on the similarity of node properties.
    Filtered KNN extends this functionality, allowing filtering on source nodes and target nodes, respectively.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.knn.filtered.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.kSpanningTree.write(G: Graph, **config: Any) -> Series[Any]

    The K-spanning tree algorithm starts from a root node and returns a spanning tree with exactly k nodes

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.labelPropagation.mutate(G: Graph, **config: Any) -> Series[Any]

    The Label Propagation algorithm is a fast algorithm for finding communities in a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.labelPropagation.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.labelPropagation.stats(G: Graph, **config: Any) -> Series[Any]

    The Label Propagation algorithm is a fast algorithm for finding communities in a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.labelPropagation.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.labelPropagation.stream(G: Graph, **config: Any) -> DataFrame

    The Label Propagation algorithm is a fast algorithm for finding communities in a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.labelPropagation.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.labelPropagation.write(G: Graph, **config: Any) -> Series[Any]

    The Label Propagation algorithm is a fast algorithm for finding communities in a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.labelPropagation.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.leiden.mutate(G: Graph, **config: Any) -> Series[Any]

    Leiden is a community detection algorithm, which guarantees that communities are well connected

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.leiden.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.leiden.stats(G: Graph, **config: Any) -> Series[Any]

    Executes the algorithm and returns result statistics without writing the result to Neo4j.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.leiden.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.leiden.stream(G: Graph, **config: Any) -> DataFrame

    Leiden is a community detection algorithm, which guarantees that communities are well connected

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.leiden.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.leiden.write(G: Graph, **config: Any) -> Series[Any]

    Leiden is a community detection algorithm, which guarantees that communities are well connected

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.leiden.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.localClusteringCoefficient.mutate(G: Graph, **config: Any) -> Series[Any]

    The local clustering coefficient is a metric quantifying how connected the neighborhood of a node is.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.localClusteringCoefficient.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.localClusteringCoefficient.stats(G: Graph, **config: Any) -> Series[Any]

    Executes the algorithm and returns result statistics without writing the result to Neo4j.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.localClusteringCoefficient.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: triangleCountProperty(G: Graph, *, , triangleCountProperty='n/a': Any) -> DataFrame

    The local clustering coefficient is a metric quantifying how connected the neighborhood of a node is.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.localClusteringCoefficient.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.localClusteringCoefficient.write(G: Graph, **config: Any) -> Series[Any]

    The local clustering coefficient is a metric quantifying how connected the neighborhood of a node is.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.localClusteringCoefficient.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.louvain.mutate(G: Graph, **config: Any) -> Series[Any]

    The Louvain method for community detection is an algorithm for detecting communities in networks.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.louvain.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.louvain.stats(G: Graph, **config: Any) -> Series[Any]

    Executes the algorithm and returns result statistics without writing the result to Neo4j.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.louvain.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.louvain.stream(G: Graph, **config: Any) -> DataFrame

    The Louvain method for community detection is an algorithm for detecting communities in networks.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.louvain.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.louvain.write(G: Graph, **config: Any) -> Series[Any]

    The Louvain method for community detection is an algorithm for detecting communities in networks.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.louvain.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.maxkcut.mutate(G: Graph, **config: Any) -> Series[Any]

    Approximate Maximum k-cut maps each node into one of k disjoint communities
    trying to maximize the sum of weights of relationships between these communities.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.maxkcut.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Approximate Maximum k-cut maps each node into one of k disjoint communities
    trying to maximize the sum of weights of relationships between these communities.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.maxkcut.stream(G: Graph, **config: Any) -> DataFrame

    Approximate Maximum k-cut maps each node into one of k disjoint communities
    trying to maximize the sum of weights of relationships between these communities.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.maxkcut.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Approximate Maximum k-cut maps each node into one of k disjoint communities
    trying to maximize the sum of weights of relationships between these communities.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.modularity.stats(G: Graph, **config: Any) -> Series[Any]

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.modularity.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: relationshipWeightProperty(G: Graph, *, , communityProperty, relationshipWeightProperty='None': Any) -> DataFrame

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.modularity.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.modularityOptimization.mutate(G: Graph, **config: Any) -> Series[Any]

    The Modularity Optimization algorithm groups the nodes in the graph by optimizing the graphs modularity.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.modularityOptimization.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.modularityOptimization.stats(G: Graph, **config: Any) -> Series[Any]

    The Modularity Optimization algorithm groups the nodes in the graph by optimizing the graphs modularity.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.modularityOptimization.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.modularityOptimization.stream(G: Graph, **config: Any) -> DataFrame

    The Modularity Optimization algorithm groups the nodes in the graph by optimizing the graphs modularity.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.modularityOptimization.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.modularityOptimization.write(G: Graph, **config: Any) -> Series[Any]

    The Modularity Optimization algorithm groups the nodes in the graph by optimizing the graphs modularity.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.modularityOptimization.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.mutate(G: Graph, **config: Any) -> Series[Any]

    The Node Similarity algorithm compares a set of nodes based on the nodes they are connected to.
    Two nodes are considered similar if they share many of the same neighbors.
    Node Similarity computes pair-wise similarities based on the Jaccard metric.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.stats(G: Graph, **config: Any) -> Series[Any]

    The Node Similarity algorithm compares a set of nodes based on the nodes they are connected to.
    Two nodes are considered similar if they share many of the same neighbors.
    Node Similarity computes pair-wise similarities based on the Jaccard metric.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function::  useComponents(G: Graph, *, , similarityCutoff='1e-42', degreeCutoff='1', upperDegreeCutoff='2147483647', topK='10', bottomK='10', topN='0', bottomN='0', relationshipWeightProperty='None', similarityMetric='JACCARD',  useComponents='false': Any) -> DataFrame

    The Node Similarity algorithm compares a set of nodes based on the nodes they are connected to.
    Two nodes are considered similar if they share many of the same neighbors.
    Node Similarity computes pair-wise similarities based on the Jaccard metric.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.write(G: Graph, **config: Any) -> Series[Any]

    The Node Similarity algorithm compares a set of nodes based on the nodes they are connected to.
    Two nodes are considered similar if they share many of the same neighbors.
    Node Similarity computes pair-wise similarities based on the Jaccard metric.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.filtered.mutate(G: Graph, **config: Any) -> Series[Any]

    The Filtered Node Similarity algorithm compares a set of nodes based on the nodes they are connected to.
    Two nodes are considered similar if they share many of the same neighbors.
    The algorithm computes pair-wise similarities based on Jaccard or Overlap metrics.
    The filtered variant supports limiting which nodes to compare via source and target node filters.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.filtered.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.filtered.stats(G: Graph, **config: Any) -> Series[Any]

    The Filtered Node Similarity algorithm compares a set of nodes based on the nodes they are connected to.
    Two nodes are considered similar if they share many of the same neighbors.
    The algorithm computes pair-wise similarities based on Jaccard or Overlap metrics.
    The filtered variant supports limiting which nodes to compare via source and target node filters.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.filtered.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.filtered.stream(G: Graph, **config: Any) -> DataFrame

    The Filtered Node Similarity algorithm compares a set of nodes based on the nodes they are connected to.
    Two nodes are considered similar if they share many of the same neighbors.
    The algorithm computes pair-wise similarities based on Jaccard or Overlap metrics.
    The filtered variant supports limiting which nodes to compare via source and target node filters.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.filtered.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.filtered.write(G: Graph, **config: Any) -> Series[Any]

    The Filtered Node Similarity algorithm compares a set of nodes based on the nodes they are connected to.
    Two nodes are considered similar if they share many of the same neighbors.
    The algorithm computes pair-wise similarities based on Jaccard or Overlap metrics.
    The filtered variant supports limiting which nodes to compare via source and target node filters.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.nodeSimilarity.filtered.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.pageRank.mutate(G: Graph, **config: Any) -> Series[Any]

    Page Rank is an algorithm that measures the transitive influence or connectivity of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.pageRank.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.pageRank.stats(G: Graph, **config: Any) -> Series[Any]

    Executes the algorithm and returns result statistics without writing the result to Neo4j.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.pageRank.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: scaler(G: Graph, *, , dampingFactor='0.85', maxIterations='20', tolerance='0.0000001', relationshipWeightProperty='None', sourceNodes='[]', scaler='None': Any) -> DataFrame

    Page Rank is an algorithm that measures the transitive influence or connectivity of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.pageRank.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.pageRank.write(G: Graph, **config: Any) -> Series[Any]

    Page Rank is an algorithm that measures the transitive influence or connectivity of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.pageRank.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.randomWalk.stats(G: Graph, **config: Any) -> Series[Any]

    Random Walk is an algorithm that provides random paths in a graph. It’s similar to how a drunk person traverses a city.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.randomWalk.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.randomWalk.stream(G: Graph, **config: Any) -> DataFrame

    Random Walk is an algorithm that provides random paths in a graph. It’s similar to how a drunk person traverses a city.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.randomWalk.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.astar.mutate(G: Graph, **config: Any) -> Series[Any]

    The A* shortest path algorithm computes the shortest path between a pair of nodes. It uses the relationship weight
    property to compare path lengths. In addition,
    this implementation uses the haversine distance as a heuristic to converge faster.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.astar.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.astar.stream(G: Graph, **config: Any) -> DataFrame

    The A* shortest path algorithm computes the shortest path between a pair of nodes. It uses the relationship weight
    property to compare path lengths. In addition,
    this implementation uses the haversine distance as a heuristic to converge faster.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.astar.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.astar.write(G: Graph, **config: Any) -> Series[Any]

    The A* shortest path algorithm computes the shortest path between a pair of nodes. It uses the relationship weight
    property to compare path lengths. In addition,
    this implementation uses the haversine distance as a heuristic to converge faster.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.astar.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.dijkstra.mutate(G: Graph, **config: Any) -> Series[Any]

    The Dijkstra shortest path algorithm computes the shortest (weighted) path between a pair of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.dijkstra.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.dijkstra.stream(G: Graph, **config: Any) -> DataFrame

    The Dijkstra shortest path algorithm computes the shortest (weighted) path between a pair of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.dijkstra.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.dijkstra.write(G: Graph, **config: Any) -> Series[Any]

    The Dijkstra shortest path algorithm computes the shortest (weighted) path between a pair of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.dijkstra.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.yens.mutate(G: Graph, **config: Any) -> Series[Any]

    The Yen's shortest path algorithm computes the k shortest (weighted) paths between a pair of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.yens.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.yens.stream(G: Graph, **config: Any) -> DataFrame

    The Yen's shortest path algorithm computes the k shortest (weighted) paths between a pair of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.yens.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.yens.write(G: Graph, **config: Any) -> Series[Any]

    The Yen's shortest path algorithm computes the k shortest (weighted) paths between a pair of nodes.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.shortestPath.yens.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.sllpa.mutate(G: Graph, **config: Any) -> Series[Any]

    The Speaker Listener Label Propagation algorithm is a fast algorithm for finding overlapping communities in a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.sllpa.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.sllpa.stats(G: Graph, **config: Any) -> Series[Any]

    The Speaker Listener Label Propagation algorithm is a fast algorithm for finding overlapping communities in a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.sllpa.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.sllpa.stream(G: Graph, **config: Any) -> DataFrame

    The Speaker Listener Label Propagation algorithm is a fast algorithm for finding overlapping communities in a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.sllpa.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.sllpa.write(G: Graph, **config: Any) -> Series[Any]

    The Speaker Listener Label Propagation algorithm is a fast algorithm for finding overlapping communities in a graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.sllpa.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.spanningTree.mutate(G: Graph, **config: Any) -> Series[Any]

    The spanning tree algorithm visits all nodes that are in the same connected component as the starting node,
    and returns a spanning tree of all nodes in the component where the total weight of the relationships is either minimized or maximized.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.spanningTree.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.spanningTree.stats(G: Graph, **config: Any) -> Series[Any]

    The spanning tree algorithm visits all nodes that are in the same connected component as the starting node,
    and returns a spanning tree of all nodes in the component
    where the total weight of the relationships is either minimized or maximized.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.spanningTree.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.spanningTree.stream(G: Graph, **config: Any) -> DataFrame

    The spanning tree algorithm visits all nodes that are in the same connected component as the starting node,
    and returns a spanning tree of all nodes in the component
    where the total weight of the relationships is either minimized or maximized.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.spanningTree.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.spanningTree.write(G: Graph, **config: Any) -> Series[Any]

    The spanning tree algorithm visits all nodes that are in the same connected component as the starting node,
    and returns a spanning tree of all nodes in the component
    where the total weight of the relationships is either minimized or maximized.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.spanningTree.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.steinerTree.mutate(G: Graph, **config: Any) -> Series[Any]

    The steiner tree algorithm accepts a source node, as well as a list of target nodes.
    It then attempts to find a spanning tree where there is a path from the source node to each target node,
    such that the total weight of the relationships is as low as possible.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.steinerTree.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.steinerTree.stats(G: Graph, **config: Any) -> Series[Any]

    The steiner tree algorithm accepts a source node, as well as a list of target nodes.
    It then attempts to find a spanning tree where there is a path from the source node to each target node,
    such that the total weight of the relationships is as low as possible.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.steinerTree.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.steinerTree.stream(G: Graph, **config: Any) -> DataFrame

    The steiner tree algorithm accepts a source node, as well as a list of target nodes.
    It then attempts to find a spanning tree where there is a path from the source node to each target node,
    such that the total weight of the relationships is as low as possible.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.steinerTree.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.steinerTree.write(G: Graph, **config: Any) -> Series[Any]

    The steiner tree algorithm accepts a source node, as well as a list of target nodes.
    It then attempts to find a spanning tree where there is a path from the source node to each target node,
    such that the total weight of the relationships is as low as possible.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.steinerTree.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.triangleCount.mutate(G: Graph, **config: Any) -> Series[Any]

    Triangle counting is a community detection graph algorithm that is used to
    determine the number of triangles passing through each node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.triangleCount.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.triangleCount.stats(G: Graph, **config: Any) -> Series[Any]

    Triangle counting is a community detection graph algorithm that is used to
    determine the number of triangles passing through each node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.triangleCount.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: maxDegree(G: Graph, *, , maxDegree='2^63^ - 1': Any) -> DataFrame

    Triangle counting is a community detection graph algorithm that is used to
    determine the number of triangles passing through each node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.triangleCount.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.triangleCount.write(G: Graph, **config: Any) -> Series[Any]

    Triangle counting is a community detection graph algorithm that is used to
    determine the number of triangles passing through each node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.triangleCount.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Triangle counting is a community detection graph algorithm that is used to
    determine the number of triangles passing through each node in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.triangles(G: Graph, **config: Any) -> DataFrame

    Triangles streams the nodeIds of each triangle in the graph.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.wcc.mutate(G: Graph, **config: Any) -> Series[Any]

    The WCC algorithm finds sets of connected nodes in an undirected graph,
    where all nodes in the same set form a connected component.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.wcc.mutate.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.wcc.stats(G: Graph, **config: Any) -> Series[Any]

    Executes the algorithm and returns result statistics without writing the result to Neo4j.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.wcc.stats.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.wcc.stream(G: Graph, **config: Any) -> DataFrame

    The WCC algorithm finds sets of connected nodes in an undirected graph,
    where all nodes in the same set form a connected component.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.wcc.stream.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.wcc.write(G: Graph, **config: Any) -> Series[Any]

    The WCC algorithm finds sets of connected nodes in an undirected graph,
    where all nodes in the same set form a connected component.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.wcc.write.estimate(G: Graph, **config: Any) -> Series[Any]

    Returns an estimation of the memory consumption for that procedure.

    |

    **Parameters:**

        * **G** - Graph

.. py:function:: gds.alpha.linkprediction.adamicAdar(node1: int, node2: int, **config: Any) -> float

    Given two nodes, calculate Adamic Adar similarity

    |

    **Parameters:**

        * **node1** - int

        * **node2** - int

.. py:function:: gds.alpha.linkprediction.commonNeighbors(node1: int, node2: int, **config: Any) -> float

    Given two nodes, returns the number of common neighbors

    |

    **Parameters:**

        * **node1** - int

        * **node2** - int

.. py:function:: gds.alpha.linkprediction.preferentialAttachment(node1: int, node2: int, **config: Any) -> float

    Given two nodes, calculate Preferential Attachment

    |

    **Parameters:**

        * **node1** - int

        * **node2** - int

.. py:function:: gds.alpha.linkprediction.resourceAllocation(node1: int, node2: int, **config: Any) -> float

    Given two nodes, calculate Resource Allocation similarity

    |

    **Parameters:**

        * **node1** - int

        * **node2** - int

.. py:function:: gds.alpha.linkprediction.sameCommunity(node1: int, node2: int, communityProperty: Optional[str] = None) -> float

    Given two nodes, indicates if they have the same community

    |

    **Parameters:**

        * **node1** - int

        * **node2** - int

        * **communityProperty** - Optional[str] = None

.. py:function:: gds.alpha.linkprediction.totalNeighbors(node1: int, node2: int, **config: Any) -> float

    Given two nodes, calculate Total Neighbors

    |

    **Parameters:**

        * **node1** - int

        * **node2** - int

