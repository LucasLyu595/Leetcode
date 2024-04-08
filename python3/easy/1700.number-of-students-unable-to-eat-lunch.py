#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#

# @lc code=start
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        zeros, ones = 0, 0
        for sandwich in students:
            if 0 == sandwich:
                zeros += 1
            else:
                ones += 1
        for i in range(len(sandwiches)):
            sandwich = sandwiches[i]
            if 0 == sandwich:
                if 0 == zeros:
                    return ones
                zeros -= 1
            else:
                if 0 == ones:
                    return zeros
                ones -= 1
        return 0     

                

# @lc code=end

