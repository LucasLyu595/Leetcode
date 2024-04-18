#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(cur: List[int], counter: Counter) -> None:
            if len(cur) == n:
                ans.append(cur[:])
                return
            for num in counter:
                if counter[num] > 0:
                    cur.append(num)
                    counter[num] -= 1
                    backtrack(cur, counter)
                    cur.pop()
                    counter[num] += 1
        backtrack([], Counter(nums))
        return ans
        
# @lc code=end

