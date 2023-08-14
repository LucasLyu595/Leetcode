#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return '0'
        if num < 0:
            res = "-"
            num = -num
        else:
            res = ""
        tmp = []
        while num > 0:
            tmp.append(str(num % 7))
            num //= 7
        return res + "".join(tmp[::-1])

        
# @lc code=end

