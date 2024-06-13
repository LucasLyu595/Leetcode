#
# @lc app=leetcode id=2037 lang=python3
#
# [2037] Minimum Number of Moves to Seat Everyone
#

# @lc code=start
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        max_pos = max(max(seats), max(students))
        diffs = [0] * max_pos
        for seat in seats:
            diffs[seat - 1] += 1
        for student in students:
            diffs[student - 1] -= 1
        carry = 0
        ans = 0
        for diff in diffs:
            ans += abs(carry)
            carry += diff
        return ans

        
# @lc code=end

