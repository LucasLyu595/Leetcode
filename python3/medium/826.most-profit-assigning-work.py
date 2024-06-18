#
# @lc app=leetcode id=826 lang=python3
#
# [826] Most Profit Assigning Work
#

# @lc code=start
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        high = max(worker)
        jobs = [0] * (high + 1)
        for i in range(len(difficulty)):
            if difficulty[i] <= high:
                jobs[difficulty[i]] = max(profit[i], jobs[difficulty[i]])
        for i in range(1, len(jobs)):
            jobs[i] = max(jobs[i], jobs[i-1])
        return sum(jobs[work] for work in worker)


        
# @lc code=end

