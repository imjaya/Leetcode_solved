class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        
        # skip leading blanks
        start = 0
        while start < len(s) and s[start] == ' ':
            start += 1
        if start == len(s): return 0
        
        # skip sign
        sign = 1
        if s[start] == '-':
            start += 1
            sign = -1
        elif s[start] == '+':
            start += 1
        
        # get numerical part
        res = 0
        for c in s[start:]:
            # get numerical value for current character. Break if non-numeric
            d = digits.get(c,None)
            if d is None: break
            
            # return INT_MIN/INT_MAX if overflow is imminent
            if sign == -1 and ((res > 214748364) or (res == 214748364 and d == 9)):
                return -2147483648
            elif sign == 1 and ((res > 214748364) or (res == 214748364 and d > 7)):
                return 2147483647
            
            # add to result
            res = res*10 + d
        
        return sign*res