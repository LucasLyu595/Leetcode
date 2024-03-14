#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        num_zeros = []
        cur = 0
        for num in nums:
            if not num:
                cur += 1
            else:
                num_zeros.append(cur)
                cur = 0
        num_zeros.append(cur)
        left = 0
        n = len(num_zeros)
        res = 0
        if not goal:
            cumulate = lambda x: x * (1+x) // 2
            return sum(map(cumulate, num_zeros))
        while left + goal < n:
            res += (1+num_zeros[left]) * (1+num_zeros[left+goal])
            left += 1
        return res


        
        
# @lc code=end

