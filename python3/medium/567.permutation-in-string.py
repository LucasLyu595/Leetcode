#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = Counter(s1)
        tmp = None
        left = 0
        n = len(map1)
        numUff = 0
        for i in range(len(s2)):
            c = s2[i]
            if c in map1:
                if not tmp:
                    tmp = map1.copy()
                    numUff = n
                    left = i
                tmp[c] -= 1
                if 0 == tmp[c]:
                    numUff -= 1
                    if 0 == numUff:
                        return True
                else:
                    while 0 > tmp[c]:
                        tmp[s2[left]] += 1
                        if 1 == tmp[s2[left]]:
                            numUff += 1
                        left += 1
            else:
                if tmp:
                    tmp = None
        return False


        
# @lc code=end

