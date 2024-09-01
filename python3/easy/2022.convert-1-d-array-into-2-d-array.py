#
# @lc app=leetcode id=2022 lang=python3
#
# [2022] Convert 1D Array Into 2D Array
#

# @lc code=start
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        if len(original) != m * n:
            return ans
        for i in range(m):
            ans.append(original[i * n : (i + 1) * n][:])
        return ans

# @lc code=end

