#
# @lc app=leetcode id=988 lang=python3
#
# [988] Smallest String Starting From Leaf
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def helper(node: Optional[TreeNode], suffix: List[int]) -> List[int]:
            if not node:
                return suffix
            cur = [node.val] + suffix
            left = helper(node.left, cur)
            right = helper(node.right, cur)
            if node.right and not node.left:
                return right
            if node.left and not node.right:
                return left
            lenL, lenR = len(left), len(right)
            for i in range(min(lenL, lenR)):
                if left[i] == right[i]:
                    continue
                if left[i] < right[i]:
                    return left
                return right
            if lenL <= lenR:
                return left
            return right
        return ''.join(chr(i+ord('a')) for i in helper(root, []))
        

        
# @lc code=end

