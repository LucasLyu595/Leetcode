#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        one = [0]
        two = []
        res = 0
        visited = [False] * (amount+1)
        visited[0] = True
        while one:
            res += 1
            for v in one:
                for coin in coins:
                    tmp = v + coin
                    if tmp == amount:
                        return res
                    elif tmp > amount:
                        continue
                    elif not visited[tmp]:
                        visited[tmp] = True
                        two.append(tmp)
            one, two = two, []
        return -1
        
# @lc code=end

