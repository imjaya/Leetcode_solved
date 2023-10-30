# There is only one valid solution, meaning there is only one node from which you can start and end.
# even if there are more than one valid start positions, it always has to be the first valid start pos.
# TC: O(N) SC: O(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        cur_gain  = 0
        answer = 0

        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]
            cur_gain += gas[i] - cost[i]
            if cur_gain < 0:
                cur_gain = 0
                answer = i + 1
        return answer if total_gain >= 0 else - 1