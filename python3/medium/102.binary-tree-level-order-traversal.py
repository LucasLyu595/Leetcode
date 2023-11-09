#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        current, next = [], []
        current.insert(0, root)
        values = []
        while len(current) != 0:
            tmp = current.pop()
            values.append(tmp.val)
            if tmp.left:
                next.insert(0, tmp.left)
            if tmp.right:
                next.insert(0, tmp.right)
            if len(current) == 0:
                current = next
                next = []
                res.append(values)
                values = []
        return res
            

        
# @lc code=end

