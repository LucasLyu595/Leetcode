#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [0] * n
        frontier = deque()
        frontier.append(source)
        while frontier:
            cur = frontier.popleft()
            visited[cur] = 1
            for neighbor in graph[cur]:
                if not visited[neighbor]:
                    if neighbor == destination:
                        return True
                    frontier.append(neighbor)
        return False


        
# @lc code=end

