#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n: int) -> int:
            sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                sum += digit ** 2
            return sum
        
        seen = set()
        while n not in seen:
            if n == 1: return True
            seen.add(n)
            n = get_next(n)
        return False

        
# @lc code=end

