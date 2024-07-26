#
# @lc app=leetcode id=1334 lang=python3
#
# [1334] Find the City With the Smallest Number of Neighbors at a Threshold Distance
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        dis = [[inf] * n for _ in range(n)]
        for u, v, weight in edges:
            if weight > distanceThreshold:
                continue
            graph[u].append(v)
            graph[v].append(u)
            dis[u][v] = weight
            dis[v][u] = weight


        ans, min_num = 0, n
        for i in range(n):
            next = deque(graph[i])
            reachable = set(next)
            while next:
                cur = next.popleft()
                for neighbor in graph[cur]:
                    if neighbor == i:
                        continue
                    tmp_dis = dis[i][cur] + dis[cur][neighbor]
                    if tmp_dis > distanceThreshold:
                        continue
                    if dis[i][neighbor] > tmp_dis:
                        dis[i][neighbor] = tmp_dis
                        reachable.add(neighbor)
                        next.append(neighbor)
            num = len(reachable)
            if num <= min_num:
                min_num = num
                ans = i
        return ans


# @lc code=end

