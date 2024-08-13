#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(start: int, path: list, prefix: int) -> None:
            nonlocal target
            for i in range(start, len(candidates)):
                cur = candidates[i]
                if i > start and cur == candidates[i-1]:
                    continue
                if prefix + cur > target:
                    return
                if prefix + cur == target:
                    ans.append(path + [cur])
                    return
                path.append(cur)
                backtrack(i+1, path, prefix + cur)
                path.pop()
        backtrack(0, [], 0)
        return ans

# @lc code=end

