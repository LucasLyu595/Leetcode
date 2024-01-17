#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        if not heights or not heights[0]:
            return res
        num_rows, num_cols = len(heights), len(heights[0])
        pacific, atlantic = [], []
        for i in range(num_rows):
            pacific.append((i, 0))
            atlantic.append((i, num_cols - 1))
        for j in range(num_cols):
            pacific.append((0, j))
            atlantic.append((num_rows - 1, j))
        
        def bfs(queue: List[int])-> set:
            reachable = set()
            while queue:
                (row, col) = queue.pop(0)
                reachable.add((row, col))
                for (i, j) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    new_row, new_col = row + i, col + j
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue
                    if (new_row, new_col) in reachable:
                        continue
                    if heights[new_row][new_col] >= heights[row][col]:
                        queue.append((new_row, new_col))
            return reachable
        pac_reachable = bfs(pacific)
        atl_reachable = bfs(atlantic)
        return list(pac_reachable.intersection(atl_reachable))
        
        
# @lc code=end

