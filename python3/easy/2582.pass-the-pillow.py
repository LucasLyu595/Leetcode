#
# @lc app=leetcode id=2582 lang=python3
#
# [2582] Pass the Pillow
#

# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        remainder = time % (2 * n - 2)
        return 1 + (remainder if remainder < n else 2 * n - remainder - 2)
        
# @lc code=end

