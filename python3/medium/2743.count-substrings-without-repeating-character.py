#
# @lc app=leetcode id=2743 lang=python3
#
# [2743] Count Substrings Without Repeating Character
#

# @lc code=start
from collections import defaultdict
class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        # Sliding window
        # Time complexity: O(N), space complexity: O(1),
        # where N = len(s).
        start = -1
        # pos[x] is the position of the last occurrence
        # of x encountered so far.
        pos = defaultdict(lambda: -1)
        ans = 0
        for end, x in enumerate(s):
            if pos[x] > start: 
                start = pos[x]
            ans += end - start
            pos[x] = end
        return ans
        
# @lc code=end

