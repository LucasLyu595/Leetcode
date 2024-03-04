#
# @lc app=leetcode id=984 lang=python3
#
# [984] String Without AAA or BBB
#

# @lc code=start
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if not tokens: return 0
        low, high = 0, len(tokens) - 1
        score = 0
        tokens.sort()
        while low <= high:
            if (power >= tokens[low]):
                score += 1
                power -= tokens[low]
                low += 1
            elif low < high and score > 0:
                score -= 1
                power += tokens[high]
                high -= 1
            else:
                return score
        return score
        
# @lc code=end

