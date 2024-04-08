#
# @lc app=leetcode id=255 lang=python3
#
# [255] Verify Preorder Sequence in Binary Search Tree
#

# @lc code=start
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_limit = -inf
        stack = []
        
        for num in preorder:
            while stack and stack[-1] < num:
                min_limit = stack.pop()
                
            if num <= min_limit:
                return False
            
            stack.append(num)
        
        return True
        

        
        
# @lc code=end

