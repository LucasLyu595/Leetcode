#
# @lc app=leetcode id=2196 lang=python3
#
# [2196] Create Binary Tree From Descriptions
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        root = set()
        for parent, child, isLeft in descriptions:
            if parent not in node_map:
                node_map[parent] = TreeNode(parent)
                root.add(parent)
            if child not in node_map:
                node_map[child] = TreeNode(child)
            if child in root:
                root.remove(child)
            if isLeft:
                node_map[parent].left = node_map[child]
            else:
                node_map[parent].right = node_map[child]
        return node_map[root.pop()]
        
# @lc code=end

