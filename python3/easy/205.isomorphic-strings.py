#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            else:
                dic[s[i]] = t[i]
        dic = {}
        for i in range(len(s)):
            if t[i] in dic:
                if dic[t[i]] != s[i]:
                    return False
            else:
                dic[t[i]] = s[i]
        return True


        
# @lc code=end

