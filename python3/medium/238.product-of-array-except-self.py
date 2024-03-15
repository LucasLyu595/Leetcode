#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zero = nums.count(0)
        mutiply = lambda a, b: a * b
        n = len(nums)
        if not num_zero:
            product = reduce(mutiply, nums)
            devide = lambda a: product // a
            return map(devide, nums)
        elif num_zero == 1:
            index = nums.index(0)
            res = [0] * n
            del nums[index]
            res[index] = reduce(mutiply, nums)
            return res
        return [0] * n
        
# @lc code=end

