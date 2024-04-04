#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        res = 0
        for c in s:
            if '(' == c:
                depth += 1
            elif ')' == c:
                depth -= 1
            if depth > res:
                res = depth
        return res
            
        
# @lc code=end

