import numpy as np
import math


class PriorityQueue:

    def __init__(self):
        pass

    def insert(self, value, priority):
        raise NotImplementedError

    def extract_root(self):
        raise NotImplementedError


class Node:

    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class BinaryHeap(PriorityQueue):

    def __init__(self, max_size):
        self.max_size = max_size
        self.heap = [None] * max_size
        self.leaf = 0  # index of the first empty leaf

    def parent(self, i):
        if i == 0:  # root is its own parent
            return 0
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value, priority):
        # insert at the end
        node = Node(value, priority)
        self.heap[self.leaf] = node
        self.leaf += 1

        # rebalance
        if self.leaf == 1:
            return
        child_idx = self.leaf - 1
        parent_idx = self.parent(child_idx)
        parent, child = self.heap[parent_idx], self.heap[child_idx]

        while parent.priority < child.priority:
            # swap
            self.swap(child_idx, parent_idx)

            # update indexes
            child_idx = parent_idx
            parent_idx = self.parent(child_idx)
            parent, child = self.heap[parent_idx], self.heap[child_idx]

    def extract_root(self):
        if self.leaf == 0:
            raise ValueError("Heap is empty")

        # extract root
        root = self.heap[0]
        self.leaf -= 1
        if self.leaf != 0:
            self.heap[0] = self.heap[self.leaf]
        else:
            self.heap[0] = None
            return root

        # rebalance
        parent_idx = 0
        left_idx = self.left(0)
        right_idx = self.right(0)
        parent, left, right = (
            self.heap[parent_idx],
            self.heap[left_idx],
            self.heap[right_idx],
        )

        # if left or right are None, create a dummy node with -inf priority
        left, right = fix_none(left, right)

        while parent.priority < left.priority or parent.priority < right.priority:
            if left.priority > right.priority:
                child_idx = left_idx
            else:
                child_idx = right_idx

            # swap with child
            self.swap(parent_idx, child_idx)

            # update indexes
            parent_idx = child_idx
            left_idx, right_idx = self.left(parent_idx), self.right(parent_idx)
            if left_idx > self.leaf - 1 or right_idx > self.leaf - 1:
                break
            parent, left, right = (
                self.heap[parent_idx],
                self.heap[left_idx],
                self.heap[right_idx],
            )
            left, right = fix_none(left, right)
        return root

    def __str__(self):
        prioritiy_list = [node.priority for node in self.heap[: self.leaf]]
        return "\n" + queue2str(prioritiy_list)


### Functions to display the queue ###


def idx2depth(idx):
    return 1 + np.floor(np.log2(idx + 1)).astype(int)


def idx2col(idx, depth):
    idx_bin = bin(idx + 1)[2:]
    idx_bin = "0" * (depth - len(idx_bin)) + idx_bin
    reverse = idx_bin[::-1]
    return int(reverse, 2) - 1


def queue2str(queue):
    if len(queue) == 0:
        return "Empty queue"

    depth = idx2depth(len(queue) - 1)
    str_mat = [[None for _ in range(2**depth - 1)] for j in range(depth)]
    len_mat = [[1 for _ in range(2**depth - 1)] for j in range(depth)]
    for idx, elem in enumerate(queue):
        row = idx2depth(idx) - 1
        col = idx2col(idx, depth)
        if elem == -math.inf:
            elem_str = " "
        else:
            elem_str = str(elem)
        str_mat[row][col] = elem_str
        len_mat[row][col] = len(str(elem))
    len_mat = np.max(np.array(len_mat), axis=0)

    result = ""
    for row in range(depth):
        for col in range(2**depth - 1):
            elem = str_mat[row][col]
            if elem is None:
                result += " " * len_mat[col]
            else:
                result += elem
        result += "\n"

    return result[:-1]


def fix_none(left, right):
    if left is None:
        left = Node(None, -math.inf)
    if right is None:
        right = Node(None, -math.inf)
    return left, right
