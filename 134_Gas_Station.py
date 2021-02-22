# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        
        
#         for i in range(0,len(gas)):
#             crossed=0
#             balance=gas[i]
#             current=i
#             while(crossed<len(gas)):
                
                
#                 if(balance<cost[current]):
#                     break
#                 else:
#                     crossed+=1
#                     current+=1
#                     if(current>=len(gas)):
#                         current=0+len(gas)-current
#                     if(current==0):
#                         balance=balance-cost[len(gas)-1]+gas[current]
                        
#                     else:
#                         balance=balance-cost[current-1]+gas[current]
#                         # print(balance)
#             if(crossed==len(gas)):
#                 return i
#         return -1
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start_gas = 0
        index = 0
        for i in range(len(gas)):
            start = gas[i] - cost[i]
            
            if tank + start < 0:
                tank = 0
                index = i + 1
            else:
                tank += start
                
            start_gas += start
        
        return index if start_gas >= 0 else -1
                        
            
            
            