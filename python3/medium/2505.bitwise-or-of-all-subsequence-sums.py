#
# @lc app=leetcode id=2505 lang=python3
#
# [2505] Bitwise OR of All Subsequence Sums
#

# @lc code=start
class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        result = 0
        prefix_sum = 0

        # Iterate through each element in the input array
        for num in nums:
            # Update the cumulative sum by adding the current element
            prefix_sum += num
            # Update the result by performing bitwise OR with the current element and the cumulative sum
            result |= num | prefix_sum

        return result
        


# @lc code=end

