class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            while ((s and s[-1] > 0) and (a < 0)):
                if (s[-1] + a < 0): 
                    s.pop()
                elif s[-1] + a > 0: 
                    break    
                else: 
                    s.pop()
                    break
            else: 
                s.append(a)        
        return s
    
    
# ```
# If left destroyed right, then no more to destroy, break
# If both destroyed, no more to destroy, break
# If right destroyed left, then there is a chance it could destroy more on the left, thus
# pop out left from stack, repeat check again
# If stack becomes empty, meaning right destroyed all left asteroids, append right to stack
# ```