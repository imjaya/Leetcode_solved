# use two variables to track cur_far, and max_far when previeously set max_far is reached then increment jump.
# TC: O(N), SC: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        max_far = 0
        jumps = 0
        cur_far = 0

        for i in range(0, len(nums) - 1):
            max_far = max(max_far, i + nums[i])
            if i == cur_far:
                jumps += 1
                cur_far = max_far
        return jumps