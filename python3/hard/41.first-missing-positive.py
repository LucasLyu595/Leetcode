#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            tmp = nums[i]
            while tmp != '*' and 0 < tmp <= n:
                next = nums[tmp-1]
                nums[tmp-1] = '*'
                tmp = next
        for i in range(n):
            if nums[i] != '*':
                return i + 1
        return n + 1
                
            
# @lc code=end

