#
# @lc app=leetcode id=2997 lang=python3
#
# [2997] Minimum Number of Operations to Make Array XOR Equal to K
#

# @lc code=start
from functools import reduce
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = reduce(lambda a, b: a ^ b, nums) ^ k
        binary_string = bin(ans)[2:]
        return sum('1' == i for i in binary_string)

        
        
# @lc code=end

