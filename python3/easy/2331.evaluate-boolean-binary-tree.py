#
# @lc app=leetcode id=2331 lang=python3
#
# [2331] Evaluate Boolean Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return False if root.val == 0 else True
        left, right = self.evaluateTree(root.left), self.evaluateTree(root.right)
        if 2 == root.val:
            return left or right
        return left and right
        
# @lc code=end

