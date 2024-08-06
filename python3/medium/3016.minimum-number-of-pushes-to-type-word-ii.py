#
# @lc app=leetcode id=3016 lang=python3
#
# [3016] Minimum Number of Pushes to Type Word II
#

# @lc code=start
class Solution:
    def minimumPushes(self, word: str) -> int:
        l=[0]*(32)
        for i in range(26):
            l[i]=word.count(chr(97+i))
        l.sort(reverse=True)
        res=0
        for i in range(4):
            for j in range(8):
                res+=(i+1)*l[8*i+j]
        return res
        
# @lc code=end

