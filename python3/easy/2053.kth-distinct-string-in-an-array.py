#
# @lc app=leetcode id=2053 lang=python3
#
# [2053] Kth Distinct String in an Array
#

# @lc code=start
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        distinct = []
        for string in arr:
            if counter[string] > 1:
                continue
            if k > 1:
                k -= 1
            else:
                distinct.append(string)
        if not distinct:
            return ""
        return distinct[0]
        
# @lc code=end

