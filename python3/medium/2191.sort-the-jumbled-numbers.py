#
# @lc app=leetcode id=2191 lang=python3
#
# [2191] Sort the Jumbled Numbers
#

# @lc code=start
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda num: int(''.join(str(mapping[int(i)]) for i in str(num))))
        
# @lc code=end

