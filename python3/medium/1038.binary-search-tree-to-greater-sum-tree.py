#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        cum = 0
        def dfs(node: TreeNode) -> None:
            nonlocal cum
            if node.right:
                dfs(node.right)
            cum += node.val
            node.val = cum
            if node.left:
                dfs(node.left)
        dfs(root)
        return root

        
# @lc code=end

