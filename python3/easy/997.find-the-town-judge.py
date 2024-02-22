#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if 1 == n: return n
        trustMap = defaultdict(list)
        trustee = set()
        for a, b in trust:
            trustMap[b].append(a)
            trustee.add(a)
        for judge in trustMap:
            if n - 1 == len(trustMap[judge]) and sum(list(trustee)) + judge == ((n+1)*n) >> 1:
                return judge
        return -1
        
        
# @lc code=end

