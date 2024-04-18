#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(cur: List[int], start: int):
            if len(cur) == k:
                ans.append(cur[:])
                return
            for i in range(start, n):
                cur.append(i+1)
                backtrack(cur, i+1)
                cur.pop()
        backtrack([], 0)
        return ans
        
# @lc code=end

