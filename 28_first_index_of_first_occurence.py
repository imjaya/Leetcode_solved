# Sliding window technique TC: O(mn) SC: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for window_start in range(n-m+1):
            for i in range(m):
                if needle[i] != haystack[window_start + i]:
                    break
                if i == m -1:
                    return window_start
        return -1 