#
# @lc app=leetcode id=1579 lang=python3
#
# [1579] Remove Max Number of Edges to Keep Graph Fully Traversable
#

# @lc code=start
class DSU:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        xset, yset = self.find(x), self.find(y)
        if xset != yset:
            if self.rank[xset] < self.rank[yset]:
                self.parent[xset] = yset
            elif self.rank[xset] > self.rank[yset]:
                self.parent[yset] = xset
            else:
                self.parent[xset] = yset
                self.rank[yset] += 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse=True)
        alice_dsu = DSU(n+1)
        bob_dsu = DSU(n+1)
        removed = 0
        alice_n_edge = 0
        bob_n_edge = 0
        for type, u, v in edges:
            if 3 == type:
                if alice_dsu.union(u, v):
                    bob_dsu.union(u, v)
                    alice_n_edge += 1
                    bob_n_edge += 1
                else:
                    removed += 1
            elif 2 == type:
                if bob_dsu.union(u, v):
                    bob_n_edge += 1
                else:
                    removed += 1
            elif 1 == type:
                if alice_dsu.union(u, v):
                    alice_n_edge += 1
                else:
                    removed += 1
        return removed if alice_n_edge == bob_n_edge == n - 1 else -1
        
# @lc code=end

