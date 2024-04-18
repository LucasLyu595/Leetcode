#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        n = len(nums)
        def backtrack(cur: List[int], start: int) -> None:
            nonlocal n
            if start == n:
                return
            for i in range(start, n):
                cur.append(nums[i])
                ans.append(cur[:])
                backtrack(cur, i+1)
                cur.pop()
        backtrack([], 0)
        return ans


        
# @lc code=end

