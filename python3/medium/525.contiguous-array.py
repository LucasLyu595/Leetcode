#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = {}, {}
        prefix = 0
        left[0] = -1
        for i in range(n):
            if 0 == nums[i]:
                prefix -= 1
            else:
                prefix += 1
            if prefix not in left:
                left[prefix] = i
            else:
                right[prefix] = i
        res = 0
        for key in right:
            res = max(res, right[key] - left[key]) 
        return res
        

        
# @lc code=end

