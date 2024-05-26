#
# @lc app=leetcode id=552 lang=python3
#
# [552] Student Attendance Record II
#

# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        
        MOD = int(1e9+7)

        '''dp0 = [[0 for _ in range(3)] for _ in range(2)]
        dp0[0][0] = 1
        for _ in range(n):
            dp1 = [[0 for _ in range(3)] for _ in range(2)]

            dp1[0][0] = (sum(dp0[0]))%MOD
            dp1[0][1], dp1[0][2] = dp0[0][0], dp0[0][1]
            dp1[1][0] = (sum(dp0[0])+sum(dp0[1]))%MOD
            dp1[1][1], dp1[1][2] = dp0[1][0], dp0[1][1]

            dp0 = dp1.copy()

        return (sum(dp0[0])+sum(dp0[1]))%MOD'''

        def matmul(A, B):
            C = [[0 for _ in range(6)] for _ in range(6)]
            for k in range(6):
                for i in range(6):
                    for j in range(6): C[i][j] = (C[i][j]+A[i][k]*B[k][j])%MOD
            return C
        
        def pow(A, n):
            if n==1: return A
            
            t = pow(A, int(n/2))
            t = matmul(t, t)

            if (n%2)==0: return t
            else: return matmul(A, t)
        
        t = pow([[1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]], n)
        
        return sum([t[i][0] for i in range(6)])%MOD

# matrix = [
# # P, L, LL, A, AP, AL, ALL
# [ 1, 1, 0, 1, 0, 0, 0 ], # P
# [ 1, 0, 1, 1, 0, 0, 0 ], # L
# [ 1, 0, 0, 1, 0, 0, 0 ], # LL
# [ 0, 0, 0, 0, 1, 1, 0 ], # A
# [ 0, 0, 0, 0, 1, 1, 0 ], # AP
# [ 0, 0, 0, 0, 1, 0, 1 ], # AL
# [ 0, 0, 0, 0, 1, 0, 0 ], # ALL
# ]
        
# @lc code=end

