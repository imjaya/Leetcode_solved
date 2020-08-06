class Solution:
    def romanToInt(self, s):
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        t = 0
        for i in range(len(s)-1):
            if(d[s[i]]>=d[s[i+1]]):
                t = t + d[s[i]]
            else:
                t = t - d[s[i]]

        try:
            t = t + d[s[i+1]]
        except:
            t = t + d[s[0]]
        return t
