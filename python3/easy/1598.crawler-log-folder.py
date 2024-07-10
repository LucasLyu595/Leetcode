#
# @lc app=leetcode id=1598 lang=python3
#
# [1598] Crawler Log Folder
#

# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if '..' in log:
                ans -= 1
                if ans < 0:
                    ans = 0
            elif '.' in log:
                continue
            else:
                ans += 1
        return ans
        
# @lc code=end

