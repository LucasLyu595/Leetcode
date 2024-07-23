#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
#

# @lc code=start
from collections import Counter, defaultdict
import heapq


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        frequency_map = defaultdict(list)
        for num in counter:
            heapq.heappush(frequency_map[counter[num]], -num)
        ans = []
        for frequency in sorted(frequency_map.keys()):
            while frequency_map[frequency]:
                num = -heapq.heappop(frequency_map[frequency])
                for _ in range(frequency):
                    ans.append(num)
        return ans

        
# @lc code=end

