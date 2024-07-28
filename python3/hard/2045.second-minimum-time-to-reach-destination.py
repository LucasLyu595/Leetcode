#
# @lc app=leetcode id=2045 lang=python3
#
# [2045] Second Minimum Time to Reach Destination
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([(1, 1)])
        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)
        dist1[1] = 0
        while q:
            node, freq = q.popleft()
            duration = dist1[node] if freq == 1 else dist2[node]
            if (duration // change) % 2:
                duration = change * (duration // change + 1) + time
            else:
                duration += time
            for neighbor in graph[node]:
                if dist1[neighbor] == -1:
                    dist1[neighbor] = duration
                    q.append((neighbor, 1))
                elif dist2[neighbor] == -1 and dist1[neighbor] != duration:
                    if neighbor == n:
                        return duration
                    dist2[neighbor] = duration
                    q.append((neighbor, 2))
        return 0

# @lc code=end

