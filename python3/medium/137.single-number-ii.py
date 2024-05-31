#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mult = 1
        n = len(nums)
        ans = 0
        for _ in range(32):
            bitSum = 0
            for i in range(n):
                if not nums[i]:
                    continue
                bitSum += nums[i] & 1
                nums[i] >>= 1
            bitSum = bitSum % 3
            ans += bitSum * mult
            mult <<= 1
        if ans >= (1 << 31):
            ans -= 1 << 32
        return ans

        
# @lc code=end

