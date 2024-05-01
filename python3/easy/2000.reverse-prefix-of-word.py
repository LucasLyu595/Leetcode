#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        right = 0
        n = len(word)
        while right < n:
            if ch == word[right]:
                break
            right += 1
        if right == n:
            return word
        return word[:right+1][::-1] + word[right+1:]

        
# @lc code=end

