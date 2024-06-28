#
# @lc app=leetcode id=2285 lang=python3
#
# [2285] Maximum Total Importance of Roads
#

# @lc code=start
from collections import Counter


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counter = Counter()
        for u, v in roads:
            counter[u] += 1
            counter[v] += 1
        ans = 0
        for v in sorted(counter.values(), key=lambda x : -x):
            ans += v * n
            n -= 1
        return ans
        
# @lc code=end

