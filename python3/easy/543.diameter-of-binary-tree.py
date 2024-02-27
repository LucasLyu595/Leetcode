#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def getdepth(self, root: Optional[TreeNode]) -> int:
        if not root: return -1
        if not root.left and not root.right: return 0
        return max(self.getdepth(root.right), self.getdepth(root.left))+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right: return 0
        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), self.getdepth(root.left) + self.getdepth(root.right) + 2)
        
        
# @lc code=end

