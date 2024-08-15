#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = [0, 0]
        for bill in bills:
            if 5 == bill:
                counter[0] += 1
            elif 10 == bill:
                counter[0] -= 1
                counter[1] += 1
            elif 20 == bill:
                counter[0] -= 1
                if counter[1] == 0:
                    counter[0] -= 2
                else:
                    counter[1] -= 1
            if counter[0] < 0:
                return False
        return True
            
        
# @lc code=end

