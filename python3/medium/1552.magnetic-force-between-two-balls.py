#
# @lc app=leetcode id=1552 lang=python3
#
# [1552] Magnetic Force Between Two Balls
#

# @lc code=start
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def checkValid(force: int) -> bool:
            res = m - 1
            next = position[0] + force
            for p in position[1:]:
                if p >= next:
                    res -= 1
                    if not res:
                        return True
                    next = p + force
            return False

        position.sort()
        if m == 2:
            return position[-1] - position[0]
        low = 1
        high = (position[-1] - position[0]) // (m - 1)
        while low < high:
            mid = (low + high + 1) // 2
            if checkValid(mid):
                low = mid
            else:
                high = mid -1
        return low        


        
# @lc code=end

