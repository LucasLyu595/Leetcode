#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = list(s)
        left = []
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == ')':
                if not left:
                    ans[i] = ''
                else:
                    left.pop()
        for i in left:
            ans[i] = ''
        return ''.join(ans)

        
# @lc code=end

