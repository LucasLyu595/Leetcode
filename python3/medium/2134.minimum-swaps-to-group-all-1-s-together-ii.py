#
# @lc app=leetcode id=2134 lang=python3
#
# [2134] Minimum Swaps to Group All 1's Together II
#

# @lc code=start
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        numOne = sum(nums)
        if numOne == 0 or numOne == 1 or numOne == n:
            return 0
        curr = 0
        for i in range(numOne):
            if nums[i]:
                curr += 1
        maxOne = curr
        for i in range(n):
            if nums[(numOne + i) % n]:
                curr += 1
            if nums[i]:
                curr -= 1
            maxOne = max(maxOne, curr)
        return numOne - maxOne

# @lc code=end

