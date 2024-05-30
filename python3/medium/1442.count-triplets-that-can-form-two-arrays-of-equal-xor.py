#
# @lc app=leetcode id=1442 lang=python3
#
# [1442] Count Triplets That Can Form Two Arrays of Equal XOR
#

# @lc code=start
from collections import Counter


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefixCounter = Counter()
        prefixCounter[0] = 1
        indexSum = Counter()
        prefix = 0
        ans = 0
        for i in range(len(arr)):
            prefix ^= arr[i]
            ans += prefixCounter[prefix] * i - indexSum[prefix]
            prefixCounter[prefix] += 1
            indexSum[prefix] += i + 1
        return ans
        
# @lc code=end

