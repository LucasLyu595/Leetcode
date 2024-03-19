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
        max_freq, max_count = 0, 1
        for key in counter:
            if max_freq < counter[key]:
                max_freq = counter[key]
                max_count = 1
            elif max_freq == counter[key]:
                max_count += 1
        return max(len(tasks), (n + 1) * (max_freq-1) + max_count)
        




        
# @lc code=end

