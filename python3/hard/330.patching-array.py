#
# @lc app=leetcode id=330 lang=python3
#
# [330] patchesing Array
#

# @lc code=start
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i, patches = 0, 0
        miss = 1
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss <<= 1
                patches += 1
        return patches



        
# @lc code=end

