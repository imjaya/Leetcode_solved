from typing import List
def longest(arr: List[int]) -> int:
    '''Returns length of the longest consecutive subsequence'''
    arr.sort()
    last = -1
    consec = 0
    max_consec = 0
    for val in arr:
        if val != last + 1:
            consec = 0
        last = val
        consec += 1
        max_consec = max(max_consec, consec)
    return max_consec
def storage_optimization(n: int, m: int, h: List[int], v: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return (longest(h) + 1) * (longest(v) + 1)
    # return 0