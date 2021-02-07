class Solution:
    def numMatchingSubseq(self, S, words):
        # D: Dictionary with indexes where each letter is seen.
        #    E.g., D['a'] = [0,3], for S = 'abcad' 
        #    Entries are always sorted, because we visit indexes in increasing order
        D = defaultdict(list)
        for i,x in enumerate(S):
            D[x].append(i)
        #
        bisect_right = bisect.bisect_right
        def match(w):
            # i: Last Matched Position (trivial initialization)
            i = -1
            for x in w:
                # k: Index in D[x] of new letter after "S[i]" (previous)
                k   = bisect_right(D[x],i) # all(val > x for val in a[i:hi])
                if k == len(D[x]):
                    # Error, D[x] is empty of values such that "x">S[i]
                    return False 
                # Update our last position
                i = D[x][k]
            return True
        res = 0
        for w in words:
            res += match(w)
        return res