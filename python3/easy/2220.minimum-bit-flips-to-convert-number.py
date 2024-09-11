#
# @lc app=leetcode id=2220 lang=python3
#
# [2220] Minimum Bit Flips to Convert Number
#

# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ss, gs = bin(start)[2:][::-1], bin(goal)[2:][::-1]
        ans = 0
        for i in range(min(len(ss), len(gs))):
            if ss[i] == gs[i]:
                continue
            ans += 1
        ans += ss[len(gs):].count('1') + gs[len(ss):].count('1')
        return ans

# @lc code=end

