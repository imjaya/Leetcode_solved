class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowel={'a':0,'e':0,'i':0,'o':0,'u':0,'A':0,'E':0,'I':0,'O':0,'U':0}
        s=list(s)
        low=0
        high=len(s)-1
        while(low<=high):
            print(low,high)
            if(s[low] in vowel and s[high] in vowel):
                s[low],s[high]=s[high],s[low]
                high-=1
                low+=1
            elif(s[low] in vowel and s[high] not in vowel):
                high-=1
            elif(s[low] not in vowel and s[high] in vowel):
                low+=1
            else:
                high-=1
                low+=1
        
        return "".join(s)
            
        