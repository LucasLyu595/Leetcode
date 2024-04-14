#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:
            return self.sumOfLeftLeaves(root.right)
        r = self.sumOfLeftLeaves(root.right)
        if root.left.left or root.left.right:
            return self.sumOfLeftLeaves(root.left) + r
        return root.left.val + r
        
# @lc code=end

