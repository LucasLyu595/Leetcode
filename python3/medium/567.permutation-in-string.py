#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        start = 0
        if n > m:
            return False
        
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        for i in range(n):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1
        
        if s1_counts == s2_counts:
            return True
        for j in range(n,m):            
            s2_counts[ord(s2[j]) - ord('a')] += 1
            s2_counts[ord(s2[start]) - ord('a')] -= 1
            start += 1

            if s1_counts == s2_counts:
                return True
        
        return False


        
# @lc code=end

