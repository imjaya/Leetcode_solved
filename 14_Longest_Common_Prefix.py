class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        #intially consider first element of list as prefix
        strs.sort(key=len)
        prefix=strs[0]
        prefix_length=len(prefix)
        for s in strs[1:]:
            while prefix!=s[0:prefix_length]:
                prefix = prefix[0:(prefix_length-1)]
                prefix_length-=1
                if prefix_length==0:
                    return ""
        return(prefix)