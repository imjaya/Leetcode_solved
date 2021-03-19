from heapq import heappop, heappush
from typing import List

def multiprocessor_system(capacity: List[int], tasks: int) -> int:
    heap = []
    for ab in capacity:
        heappush(heap, -ab)

    ans = 0
    while tasks > 0:
        ab = heappop(heap)
        ab = -ab
        tasks -= ab
        ab = ab // 2
        if ab > 0:
            heappush(heap, -ab)
        ans += 1

    return ans