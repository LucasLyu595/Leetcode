#
# @lc app=leetcode id=2392 lang=python3
#
# [2392] Build a Matrix With Conditions
#

# @lc code=start
from collections import deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:


        def topological_sort(edges: List[List[int]], n: int) -> List[int]:
            adj = [[] for _ in range(n + 1)]
            deg = [0] * (n + 1)
            order = []
            for x in edges:
                adj[x[0]].append(x[1])
                deg[x[1]] += 1
            q = deque()
            for i in range(1, n + 1):
                if deg[i] == 0:
                    q.append(i)
            while q:
                f = q.popleft()
                order.append(f)
                n -= 1
                for v in adj[f]:
                    deg[v] -= 1
                    if deg[v] == 0:
                        q.append(v)
            if n != 0:
                return []
            return order

        rowOrder = topological_sort(rowConditions, k)
        colOrder = topological_sort(colConditions, k)
        print(rowOrder, colOrder)
        if not rowOrder or not colOrder:
            return []
        matrix = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if rowOrder[i] == colOrder[j]:
                    matrix[i][j] = rowOrder[i]
        return matrix

        
# @lc code=end

