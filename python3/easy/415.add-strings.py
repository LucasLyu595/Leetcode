#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        if l1 < l2:
            num1, num2 = num2, num1
            l1, l2 = l2, l1
        # l1 >= l2
        diff = l1 - l2
        res = ''
        next = 0
        for i in range(l1-1, -1, -1):
            tmp = int(num1[i]) + next
            if i >= diff:
                tmp +=  int(num2[i - diff])
            res = str(tmp % 10) + res
            next = tmp // 10
        if next:
            res = '1' + res
        return res

        
# @lc code=end

