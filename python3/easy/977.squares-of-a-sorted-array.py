#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r= 0, len(nums)-1
        res = []
        while l<=r:
            if abs(nums[l]) <= abs(nums[r]):
                res.append(nums[r]**2)
                r-=1
            else:
                res.append(nums[l]**2)
                l+=1
        return res[::-1]
        
# @lc code=end

