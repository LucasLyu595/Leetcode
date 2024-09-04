#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#

# @lc code=start
class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [0] * n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.size[x] > self.size[y]:
                self.parent[y] = x
                self.size[x] += self.size[y]
            else:
                self.parent[x] = y
                self.size[y] += self.size[x]


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU(26)
        check_list = []
        for e in equations:
            x, y = ord(e[0]) - ord('a'), ord(e[-1]) - ord('a')
            if e[1] == '=':
                dsu.union(x, y)
            else:
                check_list.append((x, y))
        for x, y in check_list:
            x, y = dsu.find(x), dsu.find(y)
            if x == y:
                return False
        return True

        
# @lc code=end

