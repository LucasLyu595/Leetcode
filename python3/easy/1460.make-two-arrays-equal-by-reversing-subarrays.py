#
# @lc app=leetcode id=1460 lang=python3
#
# [1460] Make Two Arrays Equal by Reversing Subarrays
#

# @lc code=start
from collections import Counter


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        t, a = Counter(target), Counter(arr)
        for ele in t.keys():
            if t[ele] != a[ele]:
                return False
        return True
        
# @lc code=end

