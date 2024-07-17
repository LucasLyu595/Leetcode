#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        def dfs(cur: Optional[TreeNode], isRoot: bool = False) -> None:
            if not cur:
                return
            # cur node must not in to_delete
            if cur.left:
                if cur.left.val in to_delete:
                    dfs(cur.left, True)
                    cur.left = None
                else:
                    if isRoot:
                        ans.append(cur.left)
                    dfs(cur.left)
            if cur.right:
                if cur.right.val in to_delete:
                    dfs(cur.right, True)
                    cur.right = None
                else:
                    if isRoot:
                        ans.append(cur.right)
                    dfs(cur.right)
        if root.val not in to_delete:
            ans.append(root)
            dfs(root)
        else:
            dfs(root, True)
        return ans

        
# @lc code=end

