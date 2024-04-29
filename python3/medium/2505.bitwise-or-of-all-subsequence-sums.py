#
# @lc app=leetcode id=2505 lang=python3
#
# [2505] Bitwise OR of All Subsequence Sums
#

# @lc code=start
from functools import reduce
class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        sums = set()
        n = len(nums)
        def backtrack(sum: int, start: int) -> None:
            nonlocal n
            sums.add(sum)
            if start == n:
                return
            for i in range(start, n):
                sum += nums[i]
                backtrack(sum, i+1)
                sum -= nums[i]
        backtrack(0, 0)
        return reduce(lambda a, b: a | b, sums)

# @lc code=end

