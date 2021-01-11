class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [t % 60 for t in time]  # (t1 + t2) % 60 == 0 iff (t1 % 60 + t2 % 60) == 0 
        c = Counter(time)
        output = 0
        for t in time:
            if t == 0 or t == 30:
                output += (c[t] - 1)  # We don't want to count t itself
            else:
                output += c[60 - t]
        return output // 2  # The question asks for only pairs where i < j, here output is double counting the pairs