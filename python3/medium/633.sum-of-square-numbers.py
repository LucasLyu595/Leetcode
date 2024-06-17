#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Any positive number n is expressible as a sum of two squares 
        # if and only if the prime factorization of n, 
        # every prime of the form (4k+3) occurs an even number of times
        if not c:
            return True
        while not c & 1:
            c >>= 1
        i = 3
        while i * i <= c:
            count = 0
            while not c % i:
                count += 1
                c /= i
            if i % 4 == 3 and count & 1 != 0:
                return False
            i += 2
        return c % 4 != 3

# @lc code=end

