#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gain = [gas[i] - cost[i] for i in range(n)]
        cur = total = 0
        res = 0
        for i in range(n):
            cur += gain[i]
            total += gain[i]
            if cur < 0:
                cur = 0
                res = i + 1
        return -1 if total < 0 else res

        
# @lc code=end

