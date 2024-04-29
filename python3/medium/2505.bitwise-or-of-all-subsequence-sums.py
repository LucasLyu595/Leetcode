#
# @lc app=leetcode id=2505 lang=python3
#
# [2505] Bitwise OR of All Subsequence Sums
#

# @lc code=start
from collections import Counter
from functools import reduce
class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        sums = set()
        n = len(nums)
        def backtrack(cur: List[int], sum: int, counter: Counter) -> None:
            nonlocal n
            sums.add(sum)
            if len(cur) == n:
                return
            for num in counter:
                if counter[num] > 0:
                    cur.append(num)
                    sum += num
                    counter[num] -= 1
                    backtrack(cur, sum, counter)
                    sum -= num
                    cur.pop()
                    counter[num] += 1
        backtrack([], 0, Counter(nums))
        return reduce(lambda a, b: a | b, sums)

# @lc code=end

