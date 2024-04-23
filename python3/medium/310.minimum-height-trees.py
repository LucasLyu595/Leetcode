#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            return [i for i in range(n)]
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        leaves = []
        for k, v in graph.items():
            if len(v) == 1:
                leaves.append(k)


        numNode = n
        while numNode > 2:
            numNode -= len(leaves)
            tmp = []
            while leaves:
                cur = leaves.pop()
                neighbor = graph[cur][0]
                graph.pop(cur)
                graph[neighbor].remove(cur)
                if len(graph[neighbor]) == 1:
                    tmp.append(neighbor)
            leaves = tmp
        return leaves

# @lc code=end

