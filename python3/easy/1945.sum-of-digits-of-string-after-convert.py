#
# @lc app=leetcode id=1945 lang=python3
#
# [1945] Sum of Digits of String After Convert
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        map = {c : str(i + 1) for i, c in enumerate(ascii_lowercase)}

        def operate(num: int) -> int:
            return sum(int(c) for c in str(num))
        
        num = int(''.join(map[c] for c in s))
        for _ in range(k):
            num = operate(num)
        return num

# @lc code=end

