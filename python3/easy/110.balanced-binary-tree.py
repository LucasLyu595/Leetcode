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
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode]) -> (bool, int):
            if not root:
                return True, -1
            leftBalanced, leftHeight = helper(root.left)
            if not leftBalanced:
                return False, 0
            rightBalanced, rightHeight = helper(root.right)
            if not rightBalanced:
                return False, 0
            return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
        return helper(root)[0]

        
# @lc code=end

