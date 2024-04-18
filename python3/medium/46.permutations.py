#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(cur: List[int]) -> None:
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return
            for num in nums:
                if num not in cur:
                    cur.append(num)
                    backtrack(cur)
                    cur.pop()
            
        backtrack([])
        return ans

        
# @lc code=end

