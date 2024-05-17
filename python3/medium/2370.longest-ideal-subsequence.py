#
# @lc app=leetcode id=2370 lang=python3
#
# [2370] Longest Ideal Subsequence
#

# @lc code=start
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        
        @lru_cache(maxsize=None)
        def helper(i: int) -> int:
            nonlocal n, k
            if i == n:
                return 0
            cur = ord(s[i])
            ans = 0
            for j in range(i + 1, n):
                tmp = ord(s[j])
                if abs(cur - tmp) <= k:
                    ans = max(ans, helper(j))
            return ans + 1
        ans = 0
        for i in range(n):
            ans = max(ans, helper(i))
        return ans
            
            

        
# @lc code=end

