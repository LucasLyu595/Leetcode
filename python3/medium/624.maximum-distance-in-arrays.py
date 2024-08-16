#
# @lc app=leetcode id=624 lang=python3
#
# [624] Maximum Distance in Arrays
#

# @lc code=start
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        mi, ma = 10000, -10000
        for array in arrays:
            low, high = array[0], array[-1]
            ans = max(ans, high - mi)
            ans = max(ans, ma - low)
            mi = min(low, mi)
            ma = max(ma, high)
        return ans
        
# @lc code=end

