class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        frequencies = {}
        for item in s:
            if item in frequencies:
                frequencies[item] += 1
            else:
                frequencies[item] = 1     
        for key,value in frequencies.items():
            if value == 1:
                return (s.index(key))
                break

        return -1