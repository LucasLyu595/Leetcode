#
# @lc app=leetcode id=1701 lang=python3
#
# [1701] Average Waiting Time
#

# @lc code=start
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = customers[0][0]
        wait = 0
        for start, interval in customers:
            time = max(time, start) + interval
            wait += (time - start)
        return wait / len(customers)
        
# @lc code=end

