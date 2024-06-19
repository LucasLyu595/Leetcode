#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
from collections import Counter


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        num = m * k
        if num > len(bloomDay):
            return -1
        elif num == len(bloomDay):
            return max(bloomDay)
        counter = Counter(bloomDay)
        days = sorted(counter.keys())
        total = 0
        p = 0
        for i in range(len(days)):
            total += counter[days[i]]
            if total >= num:
                p = i
                break
        isBloom = [False] * len(bloomDay)
        numBouquets = 0
        while numBouquets < m:
            numBouquets = 0
            numAdjBlooms = 0
            if p >= len(days):
                break
            for i in range(len(bloomDay)):
                if isBloom[i]:
                    numAdjBlooms += 1
                    continue
                if days[p] >= bloomDay[i]:
                    numAdjBlooms += 1
                    isBloom[i] = True
                    continue
                numBouquets += numAdjBlooms // k
                if numBouquets >= m:
                    return days[p]
                numAdjBlooms = 0
            numBouquets += numAdjBlooms // k
            if numBouquets >= m:
                return days[p]
            p += 1
        return -1

# @lc code=end

