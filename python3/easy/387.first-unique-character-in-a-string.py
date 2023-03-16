#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        length = len(s)
        seen = set()
        for i in range(length):
            if s[i] in seen: continue
            isUniq = True
            for j in range(i + 1, length):
                if (s[i] == s[j]):
                    seen.add(s[j])
                    isUniq = False
                    break
            if isUniq: return i
        return -1
            
        
# @lc code=end

