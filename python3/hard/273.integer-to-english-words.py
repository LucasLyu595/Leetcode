#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
from collections import deque


class Solution:
    def numberToWords(self, num: int) -> str:

        def threeDigits(num: int) -> str:
            ans = deque()
            if num:
                two_digit = num % 100
                if 0 < two_digit < 20:
                    ans.appendleft(one[two_digit])
                    num //= 100
                else:
                    digit = num % 10
                    num //= 10
                    if digit:
                        ans.appendleft(one[digit])
                    if num:
                        digit = num % 10
                        num //= 10
                        if digit:
                            ans.appendleft(ten[digit])
            if num:
                ans.appendleft("Hundred")
                ans.appendleft(one[num])
            return " ".join(ans)

        units = ["Billion", "Million", "Thousand", ""]
        one = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        ten = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        ans = []
        while num:
            three = num % 1000
            num //= 1000
            unit = units.pop()
            if unit:
                ans.append(unit)
            three_digits = threeDigits(three)
            if three_digits:
                ans.append(threeDigits(three))
            elif ans:
                ans.pop()
        word = " ".join(ans[::-1])
        if not word:
            return "Zero"
        return word


        
# @lc code=end

