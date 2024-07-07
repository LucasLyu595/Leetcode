#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink, empty = numBottles, numBottles
        while empty >= numExchange:
            numBottles = empty // numExchange
            empty = empty % numExchange
            drink += numBottles
            empty += numBottles
        return drink

        
# @lc code=end

