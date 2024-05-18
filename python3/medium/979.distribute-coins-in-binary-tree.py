#
# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def diff(node: Optional[TreeNode]) -> Union[int, int]:
            if not node:
                return 0, 0
            left, right = diff(node.left), diff(node.right)
            return left[0] + right[0] + abs(left[1]) + abs(right[1]), left[1] + right[1] + node.val - 1
        return diff(root)[0]

        
# @lc code=end

