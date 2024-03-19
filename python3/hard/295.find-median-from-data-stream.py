#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import bisect
class MedianFinder:

    def __init__(self) -> None:
        self.array = []
        self.n = 0
        

    def addNum(self, num: int) -> None:
        index = bisect.bisect_left(self.array, num)
        self.array.insert(index, num)
        self.n += 1



    def findMedian(self) -> float:
        if self.n & 1:
            return self.array[self.n // 2]
        return (self.array[self.n // 2 - 1] + self.array[self.n // 2]) / 2


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

