#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        node_list = []

        def bfs(node: TreeNode) -> None:
            if not node:
                return
            if node.left:
                bfs(node.left)
            node_list.append(node)
            if node.right:
                bfs(node.right)
        bfs(root)

        def build(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            mid = start + (end - start) // 2
            node = node_list[mid]
            node.left = build(start, mid - 1)
            node.right = build(mid+1, end)
            return node
        return build(0, len(node_list) - 1)


        
# @lc code=end

