#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = right = 0
        product = nums[0]
        res = 0
        while right < n:
            if product < k:
                right += 1
                if right < n:
                    product *= nums[right]
                else:
                    break
            else:
                res += right - left
                right += 1
                product /= nums[right]
        return res

        
        
# @lc code=end

