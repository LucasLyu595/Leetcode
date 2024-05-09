#
# @lc app=leetcode id=3075 lang=python3
#
# [3075] Maximize Happiness of Selected Children
#

# @lc code=start
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        ans = 0
        i = 0
        while i < k and happiness:
            cur = happiness[-1] - i
            if cur < 0: cur = 0
            ans += cur
            happiness.pop()
            i += 1
        return ans

        
# @lc code=end

