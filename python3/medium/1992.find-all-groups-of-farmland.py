#
# @lc app=leetcode id=1992 lang=python3
#
# [1992] Find All Groups of Farmland
#

# @lc code=start
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j = 0, 0
        m, n = len(land), len(land[0])
        while i < m and j < n:
            if 0 == land[i][j]:
                j += 1
            else:
                if (i != 0 and land[i-1][j] == 1) or (j != 0 and land[i][j-1] == 1):
                    j += 1
                else:
                    y = 0
                    while 1 == land[i][j+y]:
                        y += 1
                        if j + y == n:
                            break
                    y -= 1
                    x = 0
                    while 1 == land[i+x][j+y]:
                        x += 1
                        if i + x == m:
                            break
                    x -= 1
                    ans.append([i, j, i+x, j+y])
                    j += y + 2
            
            if j >= n:
                i += 1
                j = 0
        return ans


        
# @lc code=end

