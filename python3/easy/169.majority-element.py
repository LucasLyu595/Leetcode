#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        target = length // 2
        seem = {}
        for i in nums:
            if i not in seem:
                seem[i] = 1
            else :
                seem[i] += 1
            if seem[i] > target:
                return i
        
# @lc code=end

