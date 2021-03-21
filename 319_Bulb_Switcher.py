class Solution:
    def bulbSwitch(self, n: int) -> int:
        result = 0
        current = 1

        while (current * current <=n):
            
            current +=1
            result +=1
        

        return result