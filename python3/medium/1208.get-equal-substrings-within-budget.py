#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        n = len(s)
        curDiff = 0
        diffs = []
        ans = 0
        for right in range(n):
            diff = abs(ord(t[right]) - ord(s[right]))
            curDiff += diff
            diffs.append(diff)
            while curDiff > maxCost:
                curDiff -= diffs[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

# @lc code=end

