# Design and analysis of algorithms

This project re-implements algorithms, and helps practicing :
- paradigms (greedy, dynamic programming, divide and conquer)
- implementation challenges (data structure, complexity)  

Other topics not mentionned:
- approximation algorithms, randomized algorithms, heuristic, local search, evolutionnary algorithms

*Remark: TBI stands for "to be investigated"*

## Minimum spanning tree

|                     | *Prim*                   | *Kruskal*     |
| ------------------- | ------------------------ | ------------- |
| **Paradigm**        | Greedy                   | Greedy        |
| **Data structure**  | Queues with min heap     | Union find    |
| **Complexity**      | $O(m + n \log n)$        | $O(m \log m)$ |
| **Examples of use** | Optimal covering network |

*Remark: those algorithms do not work for directed graphs, see Edmonds' algorithm in that case.*

## Shortest path

|                     | *Djikstra*           | *Bellman-Ford*      |
| ------------------- | -------------------- | ------------------- |
| **Paradigm**        | Dynamic programming  | Dynamic programming |
| **Data structure**  | Queues with min heap | TBI                 |
| **Complexity**      | $O(m \log m)$        | $O(m n)$            |
| **Examples of use** | Shortest path        |

## Max flow / min cut

|                     | *Ford-Fulkerson*                                         | *Dinitz-Edmonds-Karp* |
| ------------------- | -------------------------------------------------------- | --------------------- |
| **Paradigm**        | Greedy                                                   | Greedy                |
| **Data structure**  | TBI                                                      | TBI                   |
| **Complexity**      | $O(m f_{max}(G))$                                        | $O(n m^2)$            |
| **Examples of use** | Maximal matching in bipartite graph, scheduling problems |

## Linear programming

Simplex, $O(n^3)$