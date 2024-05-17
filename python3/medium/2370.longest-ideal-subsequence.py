#
# @lc app=leetcode id=2370 lang=python3
#
# [2370] Longest Ideal Subsequence
#

# @lc code=start
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        ans = 0
        dp = [0] * 26
        for i in range(len(s)):
            cur = ord(s[i]) - ord('a')
            tmp = 0
            for prev in range(max(0, cur - k), min(25, cur + k) + 1):
                tmp = max(tmp, dp[prev])
            dp[cur] = tmp + 1
            ans = max(ans, dp[cur])
        return ans

        
            

        
# @lc code=end

