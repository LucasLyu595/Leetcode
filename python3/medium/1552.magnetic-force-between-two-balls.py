#
# @lc app=leetcode id=1552 lang=python3
#
# [1552] Magnetic Force Between Two Balls
#

# @lc code=start
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        high = (max(position) - min(position)) // (m - 1)
        low = 1
        position.sort()
 
        def checkValid(force: int, start: int, n: int) -> bool:
            if 1 == n:
                return True
            if start == len(position):
                return False
            if force * (n - 1) > position[-1] - position[start]:
                return False
            next = start
            pos = position[start] + force
            while position[next] < pos:
                next += 1
            return checkValid(force, next, n - 1)
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if checkValid(mid, 0, m):
                ans = mid
                low = mid + 1
                continue
            high = mid - 1
        return ans


        
# @lc code=end

