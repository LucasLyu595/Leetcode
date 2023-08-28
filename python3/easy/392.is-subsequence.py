#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dic = defaultdict(list)
        for i, letter in enumerate(t):
            dic[letter].append(i)
        cur = -1
        for letter in s:
            if letter not in dic:
                return False
            l = dic[letter]
            i = bisect.bisect_right(l, cur)
            if i != len(l):
                cur = l[i]
            else:
                return False
        return True
# @lc code=end

