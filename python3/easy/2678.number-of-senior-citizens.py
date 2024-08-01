#
# @lc app=leetcode id=2678 lang=python3
#
# [2678] Number of Senior Citizens
#

# @lc code=start
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(s[11:13] > '60' for s in details)
        
# @lc code=end

