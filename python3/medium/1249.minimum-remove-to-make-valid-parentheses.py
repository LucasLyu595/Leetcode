#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        toRemove = []
        left = []
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                left.append(i)
            elif s[i] == ')':
                if not left:
                    toRemove.append(i)
                else:
                    left.pop()
        return ''.join(s[i] for i in range(n) if i not in toRemove and i not in left)

        
# @lc code=end

