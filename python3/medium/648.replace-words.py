#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        len_map = {w: len(w) for w in dictionary}
        mi, ma = min(len_map.values()), max(len_map.values())
        # mi, ma = 100, 0
        # for l in len_map.values():
        #     if l < mi:
        #         mi = l
        #     if l > ma:
        #         ma = l
        words = sentence.split()
        ans = []
        for word in words:
            cur = word
            for i in range(mi, min(ma, len(word)) + 1):
                tmp = word[:i]
                if tmp in len_map:
                    cur = tmp
                    break
            ans.append(cur)
        return " ".join(ans)


# @lc code=end

