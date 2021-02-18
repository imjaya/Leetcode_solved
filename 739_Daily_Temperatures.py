class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
#         r=0  #TLE solution
#         for i in range(0,len(T)-1):
#             count=0
#             flag=0
#             for j in range(i+1,len(T)):
#                 count+=1
#                 if(T[j]>T[i]):
#                     T[i]=count
#                     flag=1
#                     break
#             if(flag==0):
#                 T[i]=-100
                
#         T[-1]=0
#         for i in range(0,len(T)):
#             if(T[i]==-100):
#                 T[i]=0
                    
#         return T    
    
    
        
        ans = [0] * len(T) # stack based solution
        stack = [] #indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans