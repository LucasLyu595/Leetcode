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
        node_list = []
        def add(node: TreeNode) -> None:
            if not node:
                return
            add(node.right)
            node_list.append(node)
            add(node.left)
        add(root)
        cum = 0
        for node in node_list:
            cum += node.val
            node.val = cum
        return root
        

        
# @lc code=end

