#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#

# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def subarraysWithAtMostKDistinct(nums: List[int], k: int) -> int:
            ans = 0
            start = 0
            frequency = {}
            for end in range(n):
                frequency[nums[end]] = frequency.get(nums[end], 0) + 1
                while k < len(frequency):
                    frequency[nums[start]] -= 1
                    if frequency[nums[start]] == 0:
                        frequency.pop(nums[start])
                    start += 1
                ans += end - start + 1
            return ans
        return subarraysWithAtMostKDistinct(nums, k) - subarraysWithAtMostKDistinct(nums, k-1)

        
# @lc code=end

