#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        ans = []
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def getHeight(i: int, minHeight: int) -> int:
            visited = {}
            frontier = deque([i])
            visited[i] = 0
            ans = 0
            while frontier:
                cur = frontier.popleft()
                for neighbor in graph[cur]:
                    if neighbor in visited:
                        continue
                    frontier.append(neighbor)
                    visited[neighbor] = visited[cur] + 1
                    if visited[neighbor] > ans:
                        ans = visited[neighbor]
                        if ans > minHeight:
                            return ans
            return ans
        
        minHeight = getHeight(0, n)
        ans = [0]
        frontier = deque([0])
        visited = set([0])
        while frontier:
            cur = frontier.popleft()
            for neighbor in graph[cur]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                height = getHeight(neighbor, minHeight)
                if height > minHeight:
                    continue
                if height < minHeight:
                    minHeight = height
                    ans = [neighbor]
                elif height == minHeight:
                    ans.append(neighbor)
                frontier.append(neighbor)
        return ans

# @lc code=end

