#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
import heapq
from collections import deque


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        afford, rest = [], []
        for profit, cap in zip(profits, capital):
            if cap <= w:
                afford.append(-profit)
            else:
                rest.append((cap, profit))
        heapify(afford)
        rest.sort(key=lambda x: x[0])
        rest = deque(rest)
 
        def pick() -> None:
            nonlocal w
            while rest:
                cap, profit = rest.popleft()
                if cap <= w:
                    afford.append(-profit)
                    heapq.heapify(afford)
                else:
                    rest.appendleft((cap, profit))
                    break
        while k and afford:
            w -= heapq.heappop(afford)
            k -= 1
            pick()
        return w




# @lc code=end

