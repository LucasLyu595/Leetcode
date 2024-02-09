#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for num in nums[1:]:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)
    

# Your runtime beats 92.25 % of python3 submissions
# Your memory usage beats 85.71 % of python3 submissions (17 MB)
            
        
# @lc code=end

