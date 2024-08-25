#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        def helper(cur: TreeNode) -> None:
            if cur.left:
                helper(cur.left)
            if cur.right:
                helper(cur.right)
            ans.append(cur.val)
        
        helper(root)
        return ans
        
# @lc code=end

