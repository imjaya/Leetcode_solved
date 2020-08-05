class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        c = []
        while(i<j):
            if height[i]<height[j]:
                
                d = height[i]*(j-i)
                c.append(d)
                i+=1
            else:
                d = height[j]*(j-i)
                c.append(d)
                j-=1

        c.sort()
        return max(c)