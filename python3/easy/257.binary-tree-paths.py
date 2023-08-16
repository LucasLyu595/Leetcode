#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode, pre: str, res: List[str]):
        if not root.left and not root.right:
            res.append(pre+str(root.val))
        if root.left:
            self.dfs(root.left, pre+str(root.val)+"->", res)
        if root.right:
            self.dfs(root.right, pre+str(root.val)+"->", res)


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return root
        res = []
        self.dfs(root, "", res)
        return res
        
        
# @lc code=end

