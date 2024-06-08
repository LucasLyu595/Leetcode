#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                nums[j] = nums[i] + nums[j]
                nums[j] %= k
                if nums[j] == 0:
                    return True
        return False


        
# @lc code=end

