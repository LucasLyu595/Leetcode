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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def longest(node: Optional[TreeNode]) -> int:
            if not node: return 0
            nonlocal res
            leftpath, rightpath = longest(node.left), longest(node.right)
            res = max(res, leftpath + rightpath)
            return max(leftpath, rightpath) + 1
        longest(root)
        return res
# @lc code=end

