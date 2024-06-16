#
# @lc app=leetcode id=1564 lang=python3
#
# [1564] Put Boxes Into the Warehouse I
#

# @lc code=start
from collections import Counter


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        counter = Counter(boxes)
        pre = inf
        mi, ma = min(boxes), max(boxes)
        ans = 0
        for i in range(len(warehouse)):
            if warehouse[i] < pre:
                pre = warehouse[i]
            ma = min(ma, pre)
            if ma < mi:
                break
            for box in range(ma, mi - 1, -1):
                if counter[box] > 0:
                    ma = box
                    counter[box] -= 1
                    ans += 1
                    break
        return ans

# @lc code=end

