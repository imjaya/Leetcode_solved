#Horizontal scanning approach, TC: O(S(sum of length of all the wors)), SC: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
            if len(prefix) == 0:
                return ""
        return prefix
        