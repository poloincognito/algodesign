from python_implementation.algodesign.priority_queue import BinaryHeap

### Minimum Spanning Tree

# Prim algorithm implementation relies on a queue data structure
# See https://en.wikipedia.org/wiki/Priority_queue for different implementations


# I used a binary heap, see https://en.wikipedia.org/wiki/Binary_heap


def compute_mst_prim(adj_list, edges_weights, source=0):
    """Returns a minimum spanning tree of the graph using Prim's algorithm.
    The implementation is sub-optimal (not using a Fibonacci heap and queue of vertices).

    Args:
        adj_list: list of lists of integers, the adjacency list of the graph.
        edges_weights: numpy array of float, the weights of the edges of the graph.

    Returns:
        list of tuples of integers, the edges of the minimum spanning tree

    Remark: I use a list of booleans to keep track of the vertices in the MST.
    This allows a O(1) complexity to check if a vertex is in the MST.
    """

    # Initialize the MST
    mst_vertices_bool = [False] * len(adj_list)
    mst_vertices_bool[source] = True
    mst_vertices_len = 1
    mst_edges = []

    edges_queue = BinaryHeap(len(adj_list) ** 2)
    for vertex in adj_list[source]:
        edges_queue.insert((source, vertex), -edges_weights[source, vertex])

    while mst_vertices_len < len(adj_list):
        print("Queue is", edges_queue)  # DEBUG
        # Get the edge with the smallest weight
        node = edges_queue.extract_root()
        u, v = node.value
        print("Extracted", u, v, "with weight", node.priority)  # DEBUG

        # If the vertex is not in the MST, add it
        if not mst_vertices_bool[v]:
            mst_vertices_bool[v] = True
            mst_vertices_len += 1
            mst_edges.append((u, v))

            # Add the edges of the new vertex to the queue
            for vertex in adj_list[v]:
                if not mst_vertices_bool[vertex]:
                    edges_queue.insert((v, vertex), -edges_weights[v, vertex])

    return mst_edges
