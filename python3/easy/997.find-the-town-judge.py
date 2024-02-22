#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if trust == []:
            return 1 if n==1 else -1
        trust_count = [0] * (n+1)
        for a, b in trust:
            trust_count[a] -= 1
            trust_count[b] += 1
        m = max(trust_count)
        if m == n-1:
            return trust_count.index(m)
        else:
            return -1
        
        
# @lc code=end

