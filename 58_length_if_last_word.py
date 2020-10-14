class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = len(s) - 1
        res = 0
        while r >= 0 and s[r] == ' ':
            r -= 1
            
        while r >= 0:
            if s[r] != ' ':
                r -= 1
                res += 1
            else:
                break
        return res