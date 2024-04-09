#
# @lc app=leetcode id=2073 lang=python3
#
# [2073] Time Needed to Buy Tickets
#

# @lc code=start
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        round = tickets[k]
        ans = 0
        for i in range(len(tickets)):
            if i <= k:
                ans += min(tickets[i], round)
            else:
                ans += min(tickets[i], round - 1)
        return ans


        
# @lc code=end

