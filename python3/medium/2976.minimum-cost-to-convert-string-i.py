#
# @lc app=leetcode id=2976 lang=python3
#
# [2976] Minimum Cost to Convert String I
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        weights = defaultdict(lambda: inf)
        for i in range(len(original)):
            u, v, w = original[i], changed[i], cost[i]
            graph[u].append(v)
            weights[(u, v)] = min(weights[(u, v)], w)

        for node in graph:
            next = deque(graph[node])
            while next:
                cur = next.popleft()
                if cur not in graph.keys():
                    continue
                for neighbor in graph[cur]:
                    if neighbor == node:
                        continue
                    tmp_cost = weights[(node, cur)] + weights[(cur, neighbor)]
                    if tmp_cost < weights[(node, neighbor)]:
                        weights[(node, neighbor)] = tmp_cost
                        next.append(neighbor)
        ans = 0
        for i in range(len(source)):
            s, t = source[i], target[i]
            if s == t:
                continue
            if s not in graph.keys():
                return -1
            if (s, t) not in weights.keys():
                return -1
            ans += weights[(s, t)]
        return ans
 
# @lc code=end

