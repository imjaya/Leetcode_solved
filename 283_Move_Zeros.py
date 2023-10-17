class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, n = 0, len(nums)
        for fast in range(n):
            if nums[fast] == 0:
                continue
            if nums[fast] != nums[slow]:
                nums[slow] = nums[fast]
            slow += 1
                
        while slow < n:
            if nums[slow] != 0:
                nums[slow] = 0
            slow += 1
        return nums
    
# Two pointer approach made easier TC: O(N) SC: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] !=0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
