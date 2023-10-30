#Greedy approach, to start from the end of the array,
        # try to determine a position earlier to see if we canreach previous
        # goal position if so then new index is the goal. see at the end if we reach the
        # start index.
# TC: O(N) SC: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_pos = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal_pos:
                goal_pos = i
        return goal_pos == 0
        