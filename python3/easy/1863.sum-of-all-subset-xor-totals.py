#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans |= num
        return ans << (len(nums) - 1)
        
# @lc code=end

