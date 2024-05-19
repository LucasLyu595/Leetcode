#
# @lc app=leetcode id=3068 lang=python3
#
# [3068] Find the Maximum Sum of Node Values
#

# @lc code=start
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        minGain: int = inf
        odd = 0
        ans = 0
        for num in nums:
            after = num^k
            gain = after - num
            if after > num:
                ans += after
                minGain = min(minGain, gain)
                odd ^= 1
            else:
                ans += num
                minGain = min(minGain, -gain)
        if odd:
            ans -= minGain
        return ans
        
# @lc code=end

