#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_g = amount // min(coins) + 1

        @lru_cache(maxsize=None)
        def dfs(amount: int) -> int:
            if amount < 0:
                return -1
            if not amount:
                return 0
            tmp = min_g
            for coin in coins:
                res = dfs(amount - coin)
                if res != -1:
                    tmp = min(res+1, tmp)
            return tmp if tmp != min_g else -1
        
        return dfs(amount)
        
            
        
# @lc code=end

