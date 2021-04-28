class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        dp = {}
        for w in sorted(words, key=len):
            tmp = [0]
            for i in range(len(w)):
                if w[:i] + w[i+1:] in dp:
                    tmp.append(dp[w[:i] + w[i+1:]])
                dp[w] = max(tmp) + 1
        return max(dp.values())
        