#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        star: List[int] = []
        left: List[int] = []
        for i in range(len(s)):
            if '(' == s[i]:
                left.append(i)
            elif '*' == s[i]:
                star.append(i)
            elif ')' == s[i]:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        if not len(left):
            return True
        if len(left) > len(star):
            return False
        for i in range(-1, -len(left)-1, -1):
            if left[i] > star[i]:
                return False
        return True

        
        
# @lc code=end

