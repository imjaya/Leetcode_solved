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