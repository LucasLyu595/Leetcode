#
# @lc app=leetcode id=2597 lang=python3
#
# [2597] The Number of Beautiful Subsets
#

# @lc code=start
from collections import Counter


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        self.ans = 0
        no_counter = Counter()
        def backtrack(cur: list, start: int) -> None:
            nonlocal k
            n = len(nums)
            self.ans += 1
            if start == n:
                return
            for i in range(start, n):
                if nums[i] not in no_counter or no_counter[nums[i]] == 0:
                    no_counter[nums[i]+k] += 1
                    backtrack(cur + [nums[i]], i+1)
                    no_counter[nums[i]+k] -= 1
        backtrack([], 0)
        return self.ans - 1

        

        
# @lc code=end

