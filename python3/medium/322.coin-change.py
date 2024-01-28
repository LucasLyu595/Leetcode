#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([(amount, 0)])
        visited = set()
        while q:
            left, num = q.popleft()
            if not left:
                return num
            for coin in coins:
                if left - coin >= 0 and left - coin not in visited:
                    q.append((left - coin, num + 1))
                    visited.add(left - coin)
        return -1
        
            
        
# @lc code=end

