#
# @lc app=leetcode id=1580 lang=python3
#
# [1580] Put Boxes Into the Warehouse II
#

# @lc code=start
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        left, right = 0, len(warehouse) - 1
        ans = 0
        boxes = sorted(boxes, reverse=True)
        b = 0
        while left <= right:
            room = 0
            if warehouse[left] < warehouse[right]:
                room = warehouse[right]
                right -= 1
            else:
                room = warehouse[left]
                left += 1
            while b < len(boxes) and boxes[b] > room:
                b += 1
            if b == len(boxes):
                break
            b += 1
            ans += 1
        return an
        
        
# @lc code=end

