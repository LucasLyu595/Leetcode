#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in mem: return [mem[res], i]
            mem[nums[i]] = i
            
        
# @lc code=end

