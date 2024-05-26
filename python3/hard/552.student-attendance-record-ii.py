#
# @lc app=leetcode id=552 lang=python3
#
# [552] Student Attendance Record II
#

# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        currDP = [[0] * 3 for _ in range(2)]
        nextDP = [[0] * 3 for _ in range(2)]
        currDP[0][0] = 1
        for _ in range(n):
            for numAbsent in range(2):
                for consecLate in range(3):
                    # p
                    nextDP[numAbsent][0] = (nextDP[numAbsent][0] + currDP[numAbsent][consecLate]) % MOD
                    # A
                    if numAbsent < 1:
                        nextDP[numAbsent+1][0] = (nextDP[numAbsent+1][0] + currDP[numAbsent][consecLate]) % MOD
                    # L
                    if consecLate < 2:
                        nextDP[numAbsent][consecLate+1] = (nextDP[numAbsent][consecLate+1] + currDP[numAbsent][consecLate]) % MOD
            currDP = [row[:] for row in nextDP]
            nextDP = [[0] * 3 for _ in  range(2)]
        return sum(currDP[numAbsent][consecLate] for numAbsent in range(2) for consecLate in range(3)) % MOD
        
# @lc code=end

