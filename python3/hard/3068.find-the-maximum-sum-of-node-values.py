#
# @lc app=leetcode id=3068 lang=python3
#
# [3068] Find the Maximum Sum of Node Values
#

# @lc code=start
import heapq


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        diff = []
        for i, num in enumerate(nums):
            heapq.heappush(diff, (num - (num^k), i))
        while len(diff) > 1:
            left_diff, left_i = heapq.heappop(diff)
            if left_diff > 0:
                continue
            right_diff, right_i = heapq.heappop(diff)
            if left_diff + right_diff < 0:
                nums[left_i] -= left_diff
                nums[right_i] -= right_diff
        return sum(nums)

        
        

        
# @lc code=end

