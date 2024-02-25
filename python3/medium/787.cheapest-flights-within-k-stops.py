#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
        start = deque()
        start.append(src)
        cost = [float('inf')] * n
        cost[src] = 0
        is_found = False
        while k >= 0:
            next = deque()
            tmp_cost = cost.copy()
            while start:
                prev = start.popleft()
                for neighbor, one_price in graph[prev]:
                    new_price = cost[prev] + one_price
                    if new_price < tmp_cost[neighbor]:
                        if neighbor != dst:
                            next.append(neighbor)
                        else:
                            is_found = True
                        tmp_cost[neighbor] = new_price        
            k -= 1
            start = next
            cost = tmp_cost
        if is_found: return cost[dst]
        return -1



        
# @lc code=end

