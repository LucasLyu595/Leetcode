#
# @lc app=leetcode id=834 lang=python3
#
# [834] Sum of Distances in Tree
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        distances = [[-1] * n for _ in range(n)]
        for i in range(n):
            distances[i][i] = 0
        for i in range(n):
            frontier = deque([i])
            visited = set([i])
            while frontier:
                cur = frontier.popleft()
                for neighbor in graph[cur]:
                    if neighbor in visited:
                        continue
                    if -1 == distances[i][neighbor]:
                        distance = distances[i][cur]
                        distances[i][neighbor] = distance + 1
                        distances[neighbor][i] = distance + 1
                    frontier.append(neighbor)
                    visited.add(neighbor)
        return [sum(i) for i in distances]



        
# @lc code=end

