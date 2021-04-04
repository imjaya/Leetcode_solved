class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary={}
        for i in range(0,len(order)):
            dictionary[order[i]]=i
        
        for i in range(len(words) - 1):

            for j in range(len(words[i])):
                if j >= len(words[i + 1]): return False

                if words[i][j] != words[i + 1][j]:
                    if dictionary[words[i][j]] > dictionary[words[i + 1][j]]: 
                        return False
                    break

        return True
            
        