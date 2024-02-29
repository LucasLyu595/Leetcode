#
# @lc app=leetcode id=1609 lang=python3
#
# [1609] Even Odd Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        queue = deque()
        queue.append(root)
        sign = -1
        odd_even = 1
        while queue:
            next_queue = deque()
            prev = None
            while queue:
                node = queue.popleft()
                if node.val & 1 != odd_even: return False
                if prev and prev.val * sign <= node.val * sign:
                    return False
                prev = node
                if node.left: next_queue.append(node.left)
                if node.right: next_queue.append(node.right)
            sign *= -1
            odd_even = 1 - odd_even
            queue = next_queue
        return True
        
# @lc code=end

