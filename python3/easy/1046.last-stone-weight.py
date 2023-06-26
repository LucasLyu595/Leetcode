#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while stones:
            s1 = stones.pop()
            if not stones:
                return s1
            s2 = stones.pop()
            diff = s1 - s2
            if diff > 0:
                index = bisect.bisect_left(stones, diff)
                stones.insert(index, diff)
        return 0
        
# @lc code=end

