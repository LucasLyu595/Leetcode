#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        return self.findInSet(root, set(), k)
    
    def findInSet(self, node: Optional[TreeNode], nodeSet: set, k: int) -> bool:
        if not node:
            return False
        compliment = k - node.val
        if compliment in nodeSet:
            return True
        nodeSet.add(node.val)
        return self.findInSet(node.left, nodeSet, k) or self.findInSet(node.right, nodeSet, k)
        

        
# @lc code=end

