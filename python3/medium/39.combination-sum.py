#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def dfs(self, nums: List[int], target: int, path: List[int], res: List[List[int]]) -> None:
        if target == 0:
            res.append(path)
            return
        if not nums or target < nums[0]: return
        iter = target // nums[0]
        for i in range(iter+1):
            self.dfs(nums[1:], target-nums[0]*i, path+[nums[0]]*i, res)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        self.dfs(candidates, target, [], res)
        return res
        
# @lc code=end

