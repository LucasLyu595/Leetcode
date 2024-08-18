#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [0] * n  # DP array to store ugly numbers
        ugly_numbers[0] = 1  # The first ugly number is 1

        # Three pointers for the multiples of 2, 3, and 5
        i2, i3, i5 = 0, 0, 0
        next2, next3, next5 = 2, 3, 5

        # Generate ugly numbers until we reach the nth one
        for i in range(1, n):
            # Find the next ugly number as the minimum of the next multiples
            next_ugly_number = min(
                [next2, next3, next5]
            )
            ugly_numbers[i] = next_ugly_number

            # Update the corresponding pointer and next multiple
            if next_ugly_number == next2:
                i2 += 1
                next2 = ugly_numbers[i2] * 2
            if next_ugly_number == next3:
                i3 += 1
                next3 = ugly_numbers[i3] * 3
            if next_ugly_number == next5:
                i5 += 1
                next5 = ugly_numbers[i5] * 5

        return ugly_numbers[n - 1]  # Return the nth ugly number
        
# @lc code=end

