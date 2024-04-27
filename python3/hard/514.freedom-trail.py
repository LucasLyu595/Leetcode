#
# @lc app=leetcode id=514 lang=python3
#
# [514] Freedom Trail
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n, m = len(ring), len(key)
        map = defaultdict(list)
        for i in range(n):
            map[ring[i]].append(i)

        @cache
        def dfs(prevIndex: int, curKey: int) -> int:
            ans = []
            nonlocal n, m
            if curKey == m:
                return 0
            for i in map[key[curKey]]:
                tmp = abs(prevIndex - i)
                tmp = min(tmp, n-tmp)
                res = tmp + dfs(i, curKey+1)
                ans.append(res)
            ans.sort()
            return ans[0]
        return dfs(0, 0) + m


        
# @lc code=end

