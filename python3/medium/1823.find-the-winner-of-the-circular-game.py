#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque(range(1, n+1))
        while len(queue) > 1:
            counter = k - 1
            while counter:
                tmp = queue.popleft()
                queue.append(tmp)
                counter -= 1
            queue.popleft()
        return queue[0]

        
# @lc code=end

