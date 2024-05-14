#
# @lc app=leetcode id=2473 lang=python3
#
# [2473] Minimum Cost to Buy Apples
#

# @lc code=start
from collections import defaultdict
import heapq


class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        graph = defaultdict(list)
        for a, b, cost in roads:
            graph[a].append((b, cost))
            graph[b].append((a, cost))
        frontier = [(appleCost[i-1], i) for i in graph.keys()]
        heapq.heapify(frontier)
        while frontier:
            curCost, cur = heapq.heappop(frontier)
            for neighbor, cost in graph[cur]:
                newCost = (1+k) * cost + curCost
                oldCost = appleCost[neighbor-1]
                if newCost < oldCost:
                    heapq.heappush(frontier, (newCost, neighbor))
                    appleCost[neighbor-1] = newCost
        return appleCost

        
# @lc code=end

