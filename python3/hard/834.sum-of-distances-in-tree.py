#
# @lc app=leetcode id=834 lang=python3
#
# [834] Sum of Distances in Tree
#

# @lc code=start
from collections import defaultdict, deque
import copy
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        distances = [[inf] * n for _ in range(n)]
        leaves = deque()
        for i in range(n):
            distances[i][i] = 0
            if 1 == len(graph[i]):
                leaves.append(i)
        children = defaultdict(list)
        numNode = n
        while numNode > 2:
            numNode -= len(leaves) 
            tmp = deque()
            while leaves:
                cur = leaves.popleft()
                parent = graph[cur][0]
                children[parent].append(cur)
                graph[parent].remove(cur)
                if 1 == len(graph[parent]):
                    tmp.append(parent)
            leaves = tmp
        if 2 == numNode:
            a, b = leaves
            distances[a][b] = distances[b][a] = 1
        inGraph = set(leaves)
        while numNode < n:
            numNode += len(leaves)
            tmp = deque()
            while leaves:
                cur = leaves.popleft()
                for child in children[cur]:
                    tmp.append(child)
                    for node in inGraph:
                        parentDis = distances[cur][node]
                        distances[child][node] = parentDis + 1
                        distances[node][child] = parentDis + 1
                    inGraph.add(child)
            leaves = tmp
        return [sum(i) for i in distances]



# @lc code=end

