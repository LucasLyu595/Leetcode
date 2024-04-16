#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if 1 == depth:
            return TreeNode(val, root)
        def addChildren(node: Optional[TreeNode], depth: int) -> None:
            left, right = None, None
            if node:
                left, right = node.left, node.right
                if 1 == depth:
                    node.left = TreeNode(val, left, None)
                    node.right = TreeNode(val, None, right)
                    return
                addChildren(left, depth-1)
                addChildren(right, depth-1)
        addChildren(root, depth-1)
        return root


        
# @lc code=end

