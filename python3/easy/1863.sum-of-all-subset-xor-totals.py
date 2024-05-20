#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        def backtrack(cur: int, start: int) -> None:
            self.ans += cur
            for i in range(start, len(nums)):
                key = nums[i]
                backtrack(cur ^ key, i + 1)
        backtrack(0, 0)
        return self.ans
        
# @lc code=end

