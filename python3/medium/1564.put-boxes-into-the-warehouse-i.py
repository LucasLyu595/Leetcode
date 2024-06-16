#
# @lc app=leetcode id=1564 lang=python3
#
# [1564] Put Boxes Into the Warehouse I
#

# @lc code=start
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        i = 0
        ans = 0
        boxes.sort(reverse = True)
        for room in warehouse:
            while i < len(boxes) and boxes[i] > room:
                i += 1
            if i == len(boxes):
                break
            ans += 1
            i += 1
        return ans

# @lc code=end

