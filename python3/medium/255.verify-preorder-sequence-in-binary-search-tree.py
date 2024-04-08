#
# @lc app=leetcode id=255 lang=python3
#
# [255] Verify Preorder Sequence in Binary Search Tree
#

# @lc code=start
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        i = 0
        def helper(min_limit: int , max_limit: int):
            nonlocal i
            if i == len(preorder):
                return True
            
            root = preorder[i]
            if not min_limit < root < max_limit:
                return False

            i += 1
            left = helper(min_limit, root)
            right = helper(root, max_limit)
            return left or right
            
        return helper(-inf, inf)
        

        
        
# @lc code=end

