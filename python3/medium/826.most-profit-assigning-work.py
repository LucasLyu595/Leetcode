#
# @lc app=leetcode id=826 lang=python3
#
# [826] Most Profit Assigning Work
#

# @lc code=start
from collections import Counter
import heapq


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        counter = Counter(worker)
        workers = sorted(counter.keys())
        jobs = {}
        for diff, pro in zip(difficulty, profit):
            jobs[diff] = max(jobs.get(diff, 0), pro)
        difficulty = sorted(jobs.keys())
        ans = 0
        profit = []
        heapq.heapify(profit)
        j = 0
        for worker in workers:
            while j < len(difficulty) and difficulty[j] <= worker:
                if not profit or jobs[difficulty[j]] + profit[0] > 0:
                    heapq.heappush(profit, -jobs[difficulty[j]])
                j += 1
            if profit:
                ans -= profit[0] * counter[worker]
        return ans

        
# @lc code=end

