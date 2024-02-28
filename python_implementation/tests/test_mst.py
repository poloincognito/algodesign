# %%
import numpy as np
from python_implementation.algodesign.priority_queue import BinaryHeap
from python_implementation.algodesign.minimum_spanning_tree import compute_mst_prim


# %%
def test_binary_heap():
    # create queue
    queue = BinaryHeap(10)

    # insert
    queue.insert("a", 1)
    queue.insert("b", 2)
    queue.insert("c", 3)
    queue.insert("d", 2.5)
    queue.insert("e", 1.5)

    # extract
    assert queue.extract_root().value == "c"
    assert queue.extract_root().value == "d"
    assert queue.extract_root().value == "b"
    assert queue.extract_root().value == "e"
    assert queue.extract_root().value == "a"


# %%
def test_mst_prim():

    # create graph
    adj_list = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 4], [2, 3]]

    edges_weights = [[100 for _ in range(5)] for _ in range(5)]
    edges_weights[0][1] = 1
    edges_weights[0][2] = 2
    edges_weights[1][3] = 3
    edges_weights[2][3] = 4
    edges_weights[2][4] = 5
    edges_weights[3][4] = 6
    edges_weights = np.array(edges_weights)
    edges_weights = np.triu(edges_weights)

    # compute mst
    mst_edges = compute_mst_prim(adj_list, edges_weights)
    assert set(mst_edges) == [(0, 1), (0, 2), (1, 3), (2, 4)]
