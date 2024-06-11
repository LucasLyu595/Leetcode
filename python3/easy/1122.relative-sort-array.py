#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        ans = [0] * len(arr1)
        i = 0
        for ele in arr2:
            while counter[ele] > 0:
                ans[i] = ele
                counter[ele] -= 1
                i += 1
            counter.pop(ele)
        for ele in sorted(counter.keys()):
            while counter[ele] > 0:
                ans[i] = ele
                counter[ele] -= 1
                i += 1
        return ans
        
# @lc code=end

