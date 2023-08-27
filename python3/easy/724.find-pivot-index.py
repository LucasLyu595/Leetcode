#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        tmp = 0
        if total - nums[0] == 0:
            return 0
        for i in range(1, len(nums)):
            tmp += nums[i - 1]
            if tmp * 2 == total - nums[i]:
                return i
        return -1
                
        
# @lc code=end

