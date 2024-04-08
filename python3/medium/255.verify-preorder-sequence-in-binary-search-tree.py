#
# @lc app=leetcode id=255 lang=python3
#
# [255] Verify Preorder Sequence in Binary Search Tree
#

# @lc code=start
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        def check(start:int, end: int, midValue: int) -> bool:
            if start >= end:
                return True
            flag = -1
            for i in range(start, end+1):
                if flag != -1 and preorder[i] < midValue:
                    return False
                if flag == -1 and preorder[i] > midValue:
                    flag = i
                    break
            if -1 == flag:
                return check(start+1, end, preorder[start])
            return check(start+1, flag-1, preorder[start]) and check(flag+1, end, preorder[flag])
        return check(1, len(preorder)-1, preorder[0])
        

        
        
# @lc code=end

