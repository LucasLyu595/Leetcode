#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq
class MedianFinder:

    def __init__(self) -> None:
        self.heap_first = []
        self.heap_last = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap_first, -num)
        heapq.heappush(self.heap_last, -heapq.heappop(self.heap_first))
        if len(self.heap_last) - len(self.heap_first) > 1:
            heapq.heappush(self.heap_first, -heapq.heappop(self.heap_last))


    def findMedian(self) -> float:
        if len(self.heap_first) == len(self.heap_last):
            return 0.5 * (self.heap_last[0] - self.heap_first[0])
        return self.heap_last[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

