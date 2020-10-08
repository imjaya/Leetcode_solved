# TIME O(N^2) SPACE O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water=0
        left=0
        right=0
        # right=[0]*len(height)
        # left=[0]*len(height)
        for i in range(1,len(height)):
            left=max(height[0:i+1])
            right=max(height[i:])
            trapped_water+=     min(left,right)-height[i]
            print(trapped_water)
        return(trapped_water)

#TIME O(N) SPACE O(N)
if(len(height)==0):
            return 0
        trapped_water=0
        left_max=[0]*len(height)
        right_max=[0]*len(height)
        left_max[0]=height[0]
        right_max[-1]=height[-1]
        
        for i in range(1,len(height)):
            left_max[i]=max(left_max[i-1],height[i])
            
        for i in range(len(height)-2,0,-1):
            right_max[i]=max(height[i],right_max[i+1])
            
        for i in range(1,len(height)):
            trapped_water+=min(left_max[i],right_max[i])-height[i]
            #print(trapped_water)
        return(trapped_water)

    # TIME O(N) SPACE O(1)

    ans = 0
        l,r = 0 , len(height) -1
        l_max, r_max = 0,0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_max:
                    l_max = height[l]
                else:
                    ans += l_max - height[l]
                l += 1
            else:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    ans += r_max - height[r]
                r -= 1
        return ans