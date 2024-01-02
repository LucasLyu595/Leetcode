#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def mid_iter(res: List[int], root: Optional[TreeNode]) -> None:
            if root is None:
                return
            mid_iter(res, root.left)
            res.append(root.val)
            mid_iter(res, root.right)

        res = []
        mid_iter(res, root)
        return res[k-1]
        
# @lc code=end

