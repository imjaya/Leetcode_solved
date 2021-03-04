class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        remaining = set(range(len(M)))
        frointer = set()
        cir = 0
        while remaining:
            nexti = remaining.pop()
            frointer.add(nexti)
            cir += 1
            while frointer:
                print(frointer, remaining)
                curi = frointer.pop()
                remaining.discard(curi)
                for j in range(len(M[curi])):
                    if M[curi][j] == 1:
                        if j in remaining:
                            frointer.add(j)
        return cir