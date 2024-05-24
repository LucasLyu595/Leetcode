#
# @lc app=leetcode id=1255 lang=python3
#
# [1255] Maximum Score Words Formed by Letters
#

# @lc code=start
from string import ascii_lowercase
from collections import Counter


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        score_map = {letter: s for letter, s in zip(ascii_lowercase, score)}
        letters_map = Counter(letters)
        words_map = [Counter(word) for word in words]
        self.ans = 0

        def backtrack(curScore: int, start: int) -> None:
            nonlocal letters_map
            n = len(words_map)
            if start == n:
                self.ans = max(self.ans, curScore)
                return
            for i in range(start, n):
                isScore = True
                for letter, num in words_map[i].items():
                    if num > letters_map[letter]:
                        self.ans = max(self.ans, curScore)
                        isScore = False
                        break
                if isScore:
                    letters_map -= words_map[i]
                    backtrack(curScore + sum(v * score_map[k] for k, v in words_map[i].items()), i+1)
                    letters_map += words_map[i]
        backtrack(0, 0)
        return self.ans


        
# @lc code=end

