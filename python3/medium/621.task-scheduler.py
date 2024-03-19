#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        numbers = []
        heapq.heapify(numbers)
        for key in counter:
            heapq.heappush(numbers, -counter[key])
        res = 0
        cycle = n + 1
        while numbers:
            cycle = n + 1
            tmp = []
            while cycle > 0 and numbers:
                cur = -heapq.heappop(numbers)
                cycle -= 1
                cur -= 1
                if cur > 0:
                    tmp.append(cur)
            for fre in tmp:
                heapq.heappush(numbers, -fre)
            res += n + 1
        return res - cycle




        
# @lc code=end

