from collections import defaultdict
from typing import List
def shopping_patterns(products_nodes: int, products_from: List[int], products_to: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    # node -> set of neighbors
    return 0
    neighbors = defaultdict(set)
    for u, v in zip(products_from, products_to):
        neighbors[u].add(v)
        neighbors[v].add(u)
    return min((
        # each neighbors set include the other 2 in the trio,
        # which we don't count in product score
        sum(len(neighbors[x]) - 2 for x in [u, v, w])
        # all (u, v, w) where
        # - (u, v), (v, w), (u, w) are neighbors (trio)
        # - u < v < w (to avoid duplicates, as optimization)
        for u, ns in neighbors.items()
        for v in ns
        if v > u
        for w in ns
        if w > v and w in neighbors[v]
    ), default=-1)