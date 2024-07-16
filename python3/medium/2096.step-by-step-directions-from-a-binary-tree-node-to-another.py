#
# @lc app=leetcode id=2096 lang=python3
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def root2des(cur: Optional[TreeNode], val: int, path: List[str]) -> bool:
            if not cur:
                return False
            if val == cur.val:
                return True
            path.append('L')
            if root2des(cur.left, val, path):
                return True
            path[-1] = 'R'
            if root2des(cur.right, val, path):
                return True
            path.pop()
            return False
        path2start = []
        root2des(root, startValue, path2start)
        path2dest = []
        root2des(root, destValue, path2dest)
        i = 0
        for i in range(min(len(path2start), len(path2dest))):
            if path2start[i] != path2dest[i]:
                break
        if path2start and path2dest and path2start[i] == path2dest[i]:
            i += 1
        ans = ['U'] * (len(path2start) - i) + path2dest[i:]
        return ''.join(ans)

# @lc code=end

