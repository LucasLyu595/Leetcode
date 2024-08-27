#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
from collections import defaultdict
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [0] * n
        neighbors = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            neighbors[u].append((v, succProb[i]))
            neighbors[v].append((u, succProb[i]))
        graph[start_node] = 1
        pq = [(-1, start_node)]
        while pq:
            prob, cur = heapq.heappop(pq)
            if cur == end_node:
                return -prob
            for neighbor, n_prob in neighbors[cur]:
                tmp_prob = -prob * n_prob
                if tmp_prob > graph[neighbor]:
                    graph[neighbor] = tmp_prob
                    heapq.heappush(pq, (-tmp_prob, neighbor))
        return 0


# @lc code=end

