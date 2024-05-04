#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort(key=lambda x: -x)
        left, right = 0, n-1
        ans = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            left += 1
            ans += 1
        return ans


        
# @lc code=end

