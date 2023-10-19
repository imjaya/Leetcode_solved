class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ""
        maxx = 0
        for i in s:
            if i not in result:
                result += i
            else:
                maxx = len(result) if len(result) > maxx else maxx
                result = result[result.index(i) + 1:] + i
                
        maxx = len(result) if len(result) > maxx else maxx
        return maxx
      #what approach

#Two pointer sliding window approach TC: O(N) SC: O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n= len(s)
        left, right = 0, 0
        max_length = 0
        visited_chars = set()
        if n <= 1:
            return n

        while left < n:
            if right == n or s[right] in visited_chars:
                max_length = max(max_length, right - left)
                left += 1
                right = left
                visited_chars = set()
                
            else:
                visited_chars.add(s[right])
                right += 1
                
        return max(max_length, right - left )   