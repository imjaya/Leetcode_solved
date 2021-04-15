class Solution:
    def removeVowels(self, s: str) -> str:
        vowel={'a':0,'e':0,'i':0,'o':0,'u':0,'A':0,'E':0,'I':0,'O':0,'U':0}
        i=0
        while(i<len(s)):
            if(s[i] in vowel):
                s=s[:i]+s[i+1:]
            else:
                i+=1
        return s