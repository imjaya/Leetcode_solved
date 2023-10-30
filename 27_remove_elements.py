# The basic idea behind the solution is to remove the val from its original position. TC: O(N) SC: O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
        