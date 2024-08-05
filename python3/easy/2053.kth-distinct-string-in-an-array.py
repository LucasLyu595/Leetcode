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
        for string in arr:
            if counter[string] > 1:
                continue
            k -= 1
            if k == 0:
                return string
        return ""
        
# @lc code=end

