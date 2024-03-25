#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        visited = set()
        res = []
        for num in nums:
            if num in visited:
                res.append(num)
            else:
                visited.add(num)
        return res
        
# @lc code=end

