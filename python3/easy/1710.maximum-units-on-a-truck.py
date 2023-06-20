#
# @lc app=leetcode id=1710 lang=python3
#
# [1710] Maximum Units on a Truck
#

# @lc code=start
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        res = 0
        for box in boxTypes:
            if truckSize <= 0:
                break
            if truckSize > box[0]:
                res += box[0] * box[1]
            else:
                res += truckSize * box[1]
            truckSize -= box[0]
        return res

        
# @lc code=end

