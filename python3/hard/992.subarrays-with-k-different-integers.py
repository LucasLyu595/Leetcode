#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#

# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans = 0
        start = 0
        frequency = {}
        local = 0
        for num in nums:
            curFreq = frequency.get(num, 0) + 1
            if 1 == curFreq:
                k -= 1
            frequency[num] = curFreq
            if k < 0:
                frequency.pop(nums[start]) # due to the mantaince, the frequency of nums[start] is always 1
                start += 1
                k += 1
                local = 0
            if k == 0:
                while frequency.get(nums[start]) > 1: # mantain the status that every element only appear once 
                    local += 1 # really hard to think about, needs a lot of reasoning
                    frequency[nums[start]] -= 1
                    start += 1
                ans += local + 1
        return ans

        
# @lc code=end

