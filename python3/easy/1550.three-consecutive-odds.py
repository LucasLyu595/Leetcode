#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        a, b, c = arr[0] & 1, arr[1] & 1, arr[2] & 1
        i = 3
        while i < n:
            if 1 == a & b & c:
                return True
            a, b = b, c
            c = arr[i] & 1
            i += 1
        if 1 == a & b & c:
            return True
        return False

        
# @lc code=end

