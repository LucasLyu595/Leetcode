#
# @lc app=leetcode id=1653 lang=python3
#
# [1653] Minimum Deletions to Make String Balanced
#

# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        prefixA = [0] * n
        suffixB = [0] * n
        prefixA[0] = 1 if s[0] == 'a' else 0
        for i in range(1, n):
            prefixA[i] = prefixA[i-1] + (1 if s[i] == 'a' else 0)
        suffixB[n-1] = 1 if s[n-1] == 'b' else 0
        for i in range(-2, -n-1, -1):
            suffixB[i] = suffixB[i+1] + (1 if s[i] == 'b' else 0)
        ma = 0
        for i in range(n):
            ma = max(ma, prefixA[i] + suffixB[i])
        return n - ma

# @lc code=end

