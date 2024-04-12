#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, heights: List[int]) -> int:
        top = []
        tmp = 0
        for height in heights:
            if height > tmp:
                tmp = height
            top.append(tmp)
        tmp = 0
        n = len(heights)
        for i in range(-1, -n - 1, -1):
            height = heights[i]
            if height > tmp:
                tmp = height
            top[i] = min(top[i], tmp)
        tmp = 0
        for i in range(n):
            tmp += top[i] - heights[i]
        return tmp


        
# @lc code=end

