#
# @lc app=leetcode id=1469 lang=python3
#
# [1469] Find All The Lonely Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(node: Optional[TreeNode]) -> None:
            if not node:
                return
            if not node.right and not node.left:
                return
            if node.left and not node.right:
                ans.append(node.left.val)
            if node.right and not node.left:
                ans.append(node.right.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return ans
            
        
# @lc code=end

