#
# @lc app=leetcode id=988 lang=python3
#
# [988] Smallest String Starting From Leaf
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def helper(node: Optional[TreeNode], suffix: str) -> str:
            if not node:
                return suffix
            cur = chr(node.val+ord('a')) + suffix
            left = helper(node.left, cur)
            right = helper(node.right, cur)
            if node.right and not node.left:
                return right
            if node.left and not node.right:
                return left
            if left < right:
                return left
            return right
        return helper(root, '')
        

        
# @lc code=end

