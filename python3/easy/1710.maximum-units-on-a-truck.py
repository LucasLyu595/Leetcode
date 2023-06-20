#
# @lc app=leetcode id=1710 lang=python3
#
# [1710] Maximum Units on a Truck
#

# @lc code=start
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        freq, res = [0] * 1001, 0
        for box in boxTypes:
            freq[box[1]] += box[0]
        for i in range(1000, 0, -1):
            res += min(truckSize, freq[i]) * i
            truckSize -= freq[i]
            if truckSize <= 0: break
        return res

        
# @lc code=end

