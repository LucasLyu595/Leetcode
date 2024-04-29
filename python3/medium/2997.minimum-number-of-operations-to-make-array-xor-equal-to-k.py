#
# @lc app=leetcode id=2997 lang=python3
#
# [2997] Minimum Number of Operations to Make Array XOR Equal to K
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        temp = 0
        for i in nums:
            temp ^= i
        temp ^= k
        return bin(temp).count('1')

        
        
# @lc code=end

