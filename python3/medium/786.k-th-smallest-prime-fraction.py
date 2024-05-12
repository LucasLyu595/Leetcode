#
# @lc app=leetcode id=786 lang=python3
#
# [786] K-th Smallest Prime Fraction
#

# @lc code=start
import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        franctionsHeap = []
        n = len(arr)
        for i in range(n - 1):
            heapq.heappush(franctionsHeap, (arr[i] / arr[-1], i, n - 1))
        
        while k > 1:
            _, i, j = heapq.heappop(franctionsHeap)
            k -= 1
            if i < j - 1:
                heapq.heappush(franctionsHeap, (arr[i] / arr[j-1], i, j-1))
        _, i, j = heapq.heappop(franctionsHeap)
        return [arr[i], arr[j]]


            
        
# @lc code=end

