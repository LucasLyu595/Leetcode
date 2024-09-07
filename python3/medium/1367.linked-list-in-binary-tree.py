#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> bool:
            def helper(node: Optional[TreeNode], p: Optional[ListNode]) -> bool:
                if not p:
                    return True
                if not node:
                    return False
                if node.val != p.val:
                    return False
                return helper(node.left, p.next) or helper(node.right, p.next)

            if not node:
                return False
            if node.val == head.val and helper(node, head):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)

        
# @lc code=end

