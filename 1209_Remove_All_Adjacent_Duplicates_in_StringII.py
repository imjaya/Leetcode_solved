class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # unique=set(s)
        # dupli=[]
        # for i in unique:
        #     dupli.append(i*k)
        # while True:
        #     start_string = s
        #     for dup in dupli:
        #         if dup in s:
        #             s = s.replace(dup, "")
        #     if start_string == s:
        #         return s
        
        counts=[]
        i=0
        while(i<len(s)):
            if(i==0 or s[i]!=s[i-1]):
                counts.append(1)
                i+=1
            else:
                counts[-1]+=1
                if(counts[-1]==k):
                    counts.pop(-1)
                    s=s[:i-k+1]+s[i+1:]
                    i=i-k+1
                else:
                    i+=1
        return s
        
        