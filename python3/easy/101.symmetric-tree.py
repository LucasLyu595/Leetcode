#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isS(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right: return True
            if left and right and right.val == left.val:
                return isS(left.left, right.right) and isS(left.right, right.left)
            return False
        if not root: return True
        return isS(root.left, root.right)
        
# @lc code=end

