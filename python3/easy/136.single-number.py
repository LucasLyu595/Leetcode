#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniq = set()
        for num in nums:
            uniq.add(num)
        return 2 * sum(uniq) - sum(nums)
        
# @lc code=end

