#
# @lc app=leetcode id=1915 lang=python3
#
# [1915] Number of Wonderful Substrings
#

# @lc code=start
from collections import defaultdict


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        toBit = {c: 1 << i for i, c in enumerate(ascii_lowercase[:10])}
        mask = 0

        count = defaultdict(int)
        count[0] = 1

        for c in word:
            mask ^= toBit[c]
            count[mask] += 1

        res = 0
        for mask, cnt in count.items():
            res += cnt * (cnt - 1) // 2
            for i in range(10):
                mask2 = mask ^ (1 << i)
                if mask2 < mask:
                    res += cnt * count.get(mask2, 0)



# @lc code=end


