#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        
        def helper(cur: 'Node') -> None:
            if cur.children:
                for child in cur.children:
                    helper(child)
            ans.append(cur.val)
        
        if root:
            helper(root)
        return ans

# @lc code=end

