#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = []
        sentence = sentence.split()
        pref_map = {}
        for word in dictionary:
            cur = pref_map
            for char in word:
                if '*' in cur:
                    break
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            if '*' in cur:
                continue
            if cur:
                cur.clear()
            cur['*'] = word

        for word in sentence:
            cur = pref_map
            appendWord = True
            for char in word:
                if char not in cur:
                    break
                cur = cur[char]
                if '*' in cur:
                    appendWord = False
                    break
            if appendWord:
                ans.append(word)
            else:
                ans.append(cur['*'])
        return ' '.join(ans)


# @lc code=end

