#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    @cache
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.getHeight(root.right), self.getHeight(root.left)) + 1
    

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.getHeight(root.right) - self.getHeight(root.left)) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left)
        
# @lc code=end

