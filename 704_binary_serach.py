class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x,y = 0, len(nums)-1

        while x<=y:
            print(x,y)
            m = (x+y)//2
            print(m)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                x=m+1
            else:
                y=m-1
        
        return -1
        