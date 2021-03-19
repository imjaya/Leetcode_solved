def packaging(numGroups, arr):
    """
    :type numGroups: int
    :type arr: List[int]
    :rtype: int
    """
    arr.sort()

    return arr[-1] - 1 if arr[-1] > arr[-2] + 1 else arr[-1]