#
# @lc app=leetcode id=320 lang=python3
#
# [320] Generalized Abbreviation
#

# @lc code=start
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        ans = []

        def backtrack(cur: list, index: int) -> None:
            if index == len(word):
                ans.append(''.join(str(x) for x in cur))
                return
            if isinstance(cur[-1], str):
                cur.append(1)
                backtrack(cur, index+1)
                cur.pop()
            elif isinstance(cur[-1], int):
                cur[-1] += 1
                backtrack(cur, index+1)
                cur[-1] -= 1

            cur.append(word[index])
            backtrack(cur, index+1)
            cur.pop()

        backtrack([word[0]], 1)
        backtrack([1], 1)
        return ans

# @lc code=end

