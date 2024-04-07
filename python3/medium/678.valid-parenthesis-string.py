#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        open, close = 0, 0
        n = len(s)
        for i in range(n):
            left = s[i]
            if '(' == left or '*' == left:
                open += 1
            else:
                open -= 1
            if open < 0:
                return False
            right = s[n - i - 1]
            if ')' == right or '*' == right:
                close += 1
            else:
                close -= 1
            if close < 0:
                return False
        return True

        
        
# @lc code=end

