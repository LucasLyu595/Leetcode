#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0: -1}
        prev = 0
        for i in range(len(nums)):
            prev = (prev + nums[i]) % k
            if prev in seen:
                if i - seen[prev] > 1:
                    return True
            else:
                seen[prev] = i
        return False

        
# @lc code=end

