#
# @lc app=leetcode id=1530 lang=python3
#
# [1530] Number of Good Leaf Nodes Pairs
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        parent_map = {}
        leaves = []

        def dfs(cur: TreeNode) -> None:
            if not cur.left and not cur.right:
                leaves.append(cur)
            if cur.left:
                dfs(cur.left)
                parent_map[cur.left] = cur
            if cur.right:
                dfs(cur.right)
                parent_map[cur.right] = cur
        dfs(root)
        ans = 0
        for leaf in leaves:
            good_pair = set()
            frontier = []
            if leaf in parent_map:
                frontier.append(parent_map[leaf])
            n = distance - 1
            while n:
                next = set()
                for node in frontier:
                    if node in parent_map:
                        next.add(parent_map[node])
                    if node in leaves:
                        good_pair.add(node)
                    else:
                        if node.left and node.left != leaf:
                            next.add(node.left)
                        if node.right and node.right != leaf:
                            next.add(node.right)
                frontier = list(next)
                n -= 1
            for node in frontier:
                if node in leaves:
                    good_pair.add(node)
            ans += len(good_pair)
        return ans // 2


        
# @lc code=end

