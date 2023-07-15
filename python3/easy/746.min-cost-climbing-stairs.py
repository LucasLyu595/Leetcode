#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        l = len(cost)
        if l < 2:
            return cost[0]
        if l < 3:
            return min(cost[0], cost[1])
        dp = [0]* 3
        for i in range(2, len(cost)+1):
            dp[2] = min(dp[1] + cost[i-1], dp[0] + cost[i-2])
            dp[0], dp[1] = dp[1], dp[2]
        return dp[1]
        
# @lc code=end

