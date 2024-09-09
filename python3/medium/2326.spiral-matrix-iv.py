#
# @lc app=leetcode id=2326 lang=python3
#
# [2326] Spiral Matrix IV
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1] * n for _ in range(m)]
        x, y = 0, 0
        dirs = [0, 1, 0, -1, 0]
        di = 0
        cur = head
        while cur:
            ans[x][y] = cur.val
            nx, ny = x + dirs[di], y + dirs[di+1]
            if min(nx, ny) < 0 or nx >= m or ny >= n or ans[nx][ny] >= 0:
                di = (di + 1) % 4
                nx, ny = x + dirs[di], y + dirs[di+1]
            x, y = nx, ny
            cur = cur.next
        return ans

# @lc code=end

