#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[0] * n for _ in range(n)]
        neighbors = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            neighbors[u].append(v)
            neighbors[v].append(u)
            graph[u][v] = succProb[i]
            graph[v][u] = succProb[i]
        frontier = neighbors[start_node][:]
        while frontier:
            next = []
            while frontier:
                cur = frontier.pop(0)
                for neighbor in neighbors[cur]:
                    if start_node == neighbor:
                        continue
                    tmp_prob = graph[start_node][cur] * graph[cur][neighbor]
                    if tmp_prob > graph[start_node][neighbor]:
                        graph[start_node][neighbor] = tmp_prob
                        next.append(neighbor)
            frontier = next
        return graph[start_node][end_node]

# @lc code=end

