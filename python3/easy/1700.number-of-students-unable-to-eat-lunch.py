#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#

# @lc code=start
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        difference = students.count(0) - sandwiches.count(0)
        if not difference:
            return 0
        def findKEle(array: List[int], element: int, k: int) -> int:
            for i in range(-1, -len(array) - 1, -1):
                if array[i] == element:
                    k -= 1
                if 0 == k:
                    return -i
            return -1
        return findKEle(sandwiches, int(difference > 0), abs(difference))
# @lc code=end

