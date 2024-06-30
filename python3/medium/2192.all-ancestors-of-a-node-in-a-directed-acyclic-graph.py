#
# @lc app=leetcode id=2192 lang=python3
#
# [2192] All Ancestors of a Node in a Directed Acyclic Graph
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        roots = deque()
        for i in range(n):
            if in_degree[i]:
                continue
            roots.append(i)
        ance_sets = [set() for _ in range(n)]
        while roots:
            next = deque()
            while roots:
                curr = roots.popleft()
                for child in graph[curr]:
                    ance_sets[child].update(ance_sets[curr])
                    ance_sets[child].add(curr)
                    in_degree[child] -= 1
                    if not in_degree[child]:
                        next.append(child)
            roots = next
        ans = []
        for ance in ance_sets:
            ans.append(sorted(list(ance)))
        return ans
        
# @lc code=end

