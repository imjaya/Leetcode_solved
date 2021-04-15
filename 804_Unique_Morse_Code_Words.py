class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
               "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha="abcdefghijklmnopqrstuvwxyz"
        dic={}
        for i in range(26):
            dic[alpha[i]]=morse[i]
        result=[]
        count=0
        for i in range(len(words)):
            curr=""
            for j in words[i]:
                # print()
                curr+=dic[j]
            if(curr not in result):
                result.append(curr)
        return len(result)
        
        