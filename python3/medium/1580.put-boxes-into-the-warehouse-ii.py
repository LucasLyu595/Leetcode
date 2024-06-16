#
# @lc app=leetcode id=1580 lang=python3
#
# [1580] Put Boxes Into the Warehouse II
#

# @lc code=start
from collections import Counter
import bisect


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        left, right = 0, len(warehouse) - 1
        house = [0] * len(warehouse)
        h = right
        left_prev, right_prev = inf, inf
        while left <= right:
            if warehouse[left] < warehouse[right]:
                if warehouse[right] < right_prev:
                    right_prev = warehouse[right]
                house[h] = right_prev
                right -= 1
            else:
                if warehouse[left] < left_prev:
                    left_prev = warehouse[left]
                house[h] = left_prev
                left += 1
            h -= 1
        counter = Counter(boxes)
        mi, ma = min(boxes), max(boxes)
        h = 0
        ans = 0
        usedup = False
        for box in range(mi, ma+1):
            while counter[box] > 0:
                deviation = bisect.bisect_left(house[h:], box)
                h += deviation
                if h >= len(house):
                    usedup = True
                    break
                h += 1
                counter[box] -= 1
                ans += 1
            if usedup:
                break
        return ans
        
        
# @lc code=end

