#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root: Optional[TreeNode], res: List[int]):
            if root is None:
                return
            inorder(root.left, res)  # Use 'self.inorder' here
            res.append(root.val)
            inorder(root.right, res)  # Use 'self.inorder' here

        res = []
        inorder(root, res)

        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True

        
# @lc code=end

