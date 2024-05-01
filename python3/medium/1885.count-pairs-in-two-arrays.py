#
# @lc app=leetcode id=1885 lang=python3
#
# [1885] Count Pairs in Two Arrays
#

# @lc code=start
from collections import Counter


class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        diff = [u - v for u, v in zip(nums1, nums2)]
        counter = Counter(diff)
        m = len(counter)
        diff = [k for k in counter]
        diff.sort()
        ans = 0
        left, right = 0, m - 1
        sum = 0
        suffix = [0] * m
        while left < right:
            if diff[left] + diff[right] < 0:
                left += 1
                continue
            if diff[left] + diff[right] > 0:
                ans += counter[diff[left]] * counter[diff[right]]
            sum += counter[diff[right]]
            suffix[right] = sum
            right -= 1
        while diff[left] < 0:
            left += 1
        for i in range(left, m):
            cur = counter[diff[i]]
            if diff[i] > 0:
                ans += cur * (cur-1) // 2 
            if i < m - 1:
                ans += cur * suffix[i+1]
        return ans



# @lc code=end

