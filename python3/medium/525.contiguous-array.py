#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        first = {}
        prefix = 0
        first[0] = -1
        res = 0
        for i in range(n):
            if 0 == nums[i]:
                prefix -= 1
            else:
                prefix += 1
            if prefix not in first:
                first[prefix] = i
            else:
                res = max(res, i - first[prefix])
        return res
        

        
# @lc code=end

