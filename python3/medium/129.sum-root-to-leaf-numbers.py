#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node: Optional[TreeNode], prefix: int) -> int:
            if not node:
                return 0
            cur = prefix * 10 + node.val
            if not node.left and not node.right:
                return cur
            return helper(node.left, cur) + helper(node.right, cur)
        return helper(root, 0)
        
# @lc code=end

