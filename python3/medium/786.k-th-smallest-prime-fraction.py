#
# @lc app=leetcode id=786 lang=python3
#
# [786] K-th Smallest Prime Fraction
#

# @lc code=start
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        franctions = []
        n = len(arr)
        for i in range(n-1):
            for j in range(i+1, n):
                franctions.append((arr[i], arr[j]))
        franctions.sort(key=lambda x: x[0] / x[1])
        return franctions[k-1]


            
        
# @lc code=end

