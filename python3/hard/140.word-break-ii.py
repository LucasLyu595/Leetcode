#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dictTree = {}
        for word in wordDict:
            cur = dictTree
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['*'] = None
        ans = []

        def backtrack(cur: list, start: int) -> None:
            n = len(s)
            if start == n:
                ans.append(' '.join(cur))
                return
            word = []
            node = dictTree
            for i in range(start, n):
                if s[i] not in node:
                    return
                word.append(s[i])
                node = node[s[i]]
                if '*' in node:
                    cur.append(''.join(word))
                    backtrack(cur, i + 1)
                    cur.pop()
        backtrack([], 0)
        return ans


# @lc code=end

