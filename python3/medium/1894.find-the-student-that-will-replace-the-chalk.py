#
# @lc app=leetcode id=1894 lang=python3
#
# [1894] Find the Student that Will Replace the Chalk
#

# @lc code=start
import bisect


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix = [0] * len(chalk)
        prefix[0] = chalk[0]
        for i in range(1, len(chalk)):
            prefix[i] = chalk[i] + prefix[i - 1]
        sum = prefix[-1]
        k %= sum
        return bisect.bisect_right(prefix, k)

# @lc code=end

