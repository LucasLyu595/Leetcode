#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def transform(self, string: str) -> str:
        i = 0
        res = []
        dic = {}
        for letter in string:
            if letter not in dic:
                dic[letter] = str(i)
                i += 1
            res.append(dic[letter])
        return ' '.join(res)
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transform(s) == self.transform(t)

        
# @lc code=end

