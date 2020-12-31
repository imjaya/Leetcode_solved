class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if('b' not in text or 'a' not in text or 'l' not in text or 'o' not in text or 'n' not in text):
            return 0
        freq = {} 
        for item in text: 
            if (item in freq): 
                freq[item] += 1
            else: 
                freq[item] = 1
                
        print(freq)
        count=0
        # print(freq['b'])
        print(int(min(freq['b'],freq['a'],freq['l']/2,freq['o']/2,freq['n'])))
#         while(freq['b']>=1 and freq['a']>=1 and freq['l']>=2 and freq['o']>=2 and freq['n']>=1):
#             count=count+1
#             freq['b']-=1
#             freq['a']-=1
#             freq['l']-=2
#             freq['o']-=2
#             freq['n']-=1
#             # print(freq)    
        
#         return count
        return(int(min(freq['b'],freq['a'],freq['l']/2,freq['o']/2,freq['n']))) 
            