#
# @lc app=leetcode id=592 lang=python3
#
# [592] Fraction Addition and Subtraction
#

# @lc code=start
import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        def helper(na: int, da: int, nb: int, db: int) -> tuple:
            d = da * db
            n = na * db + nb * da
            g = math.gcd(d, n)
            return (n // g, d // g)
        
        n, d = 0, 1
        i = 0
        while i < len(expression):
            neg = False
            if expression[i] == '-':
                neg = True
                i += 1
            if expression[i] == '+':
                i += 1
            nc, dc = 0, 0
            while i < len(expression) and expression[i].isdigit():
                nc = nc * 10 + int(expression[i])
                i += 1
            
            i += 1

            while i < len(expression) and expression[i].isdigit():
                dc = dc * 10 + int(expression[i])
                i += 1
            
            n, d = helper(n, d, -1 * nc if neg else nc, dc)
        return str(n) + '/' + str(d)

# @lc code=end

