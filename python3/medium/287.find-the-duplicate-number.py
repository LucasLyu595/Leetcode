#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return (sum(nums) - sum(set(nums))) // (len(nums) - len(set(nums))) 
        
# @lc code=end

