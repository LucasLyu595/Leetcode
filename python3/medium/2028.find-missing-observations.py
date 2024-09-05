#
# @lc app=leetcode id=2028 lang=python3
#
# [2028] Find Missing Observations
#

# @lc code=start
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        remain = mean * (len(rolls) + n) - sum(rolls)
        if remain > 6 * n or remain < n:
            return []
        new_mean = remain // n
        ans = [new_mean] * n
        index = 0
        total = sum(ans)
        while total < remain:
            diff = min(6 - ans[index], remain - total)
            ans[index] += diff
            total += diff
            index += 1
        return ans
        
# @lc code=end

