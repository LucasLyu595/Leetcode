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
        inOrder = []
        self.inOrderTraverse(root, inOrder)
        l, r = 0, len(inOrder) - 1
        while l < r:
            sum = inOrder[l] + inOrder[r]
            if sum == k:
                return True
            if sum < k:
                l += 1
            else:
                r -= 1
        return False
    
    def inOrderTraverse(self, node: Optional[TreeNode], list: list):
        if not node:
            return
        self.inOrderTraverse(node.left, list)
        list.append(node.val)
        self.inOrderTraverse(node.right, list)
        

        
# @lc code=end

# Accepted
# 423/423 cases passed (101 ms)
# Your runtime beats 35.68 % of python3 submissions
# Your memory usage beats 29.65 % of python3 submissions (22.6 MB)

