#
# @lc app=leetcode id=305 lang=python3
#
# [305] Number of Islands II
#

# @lc code=start
class UFS:
    def __init__(self, n) -> None:
        self.root = list(range(n))
        self.rank = [1] * n
        self.numIsland = 0 
    
    def find(self, x: int) -> None:
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                root_x, root_y = root_y, root_x
            # Modify the root of the smaller group as the root of the
            # larger group, also increment the size of the larger group.
            self.rank[root_y] += self.rank[root_x]
            self.root[root_x] = root_y
            self.numIsland -= 1
    
    def add(self) -> None:
        self.numIsland += 1

    def getNumIsland(self) -> int:
        return self.numIsland

        


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        map = [[0] * n for _ in range(m)]
        u = UFS(m*n)
        ans = []
        getIndex = lambda a, b: a*n + b
        for x, y in positions:
            if not map[x][y]:
                map[x][y] = 1
                cur = getIndex(x, y)
                u.add()
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    neighbor = getIndex(x+i, y+j)
                    if 0 <= x + i < m and 0 <= y + j < n and map[x+i][y+j] and u.find(cur) != u.find(neighbor):
                        u.union(cur, neighbor)
            ans.append(u.getNumIsland())
        return ans


        
# @lc code=end

