#
# @lc app=leetcode id=1289 lang=python3
#
# [1289] Minimum Falling Path Sum II
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # Save the size of the square grid
        n = len(grid)

        # Minimum and Second Minimum Column Index
        next_min1_c = None
        next_min2_c = None

        # Minimum and Second Minimum Value
        next_min1 = None
        next_min2 = None
        
        # Find the minimum and second minimum from the last row
        for col in range(n):
            if next_min1 is None or grid[n - 1][col] <= next_min1:
                next_min2 = next_min1
                next_min2_c = next_min1_c
                next_min1 = grid[n - 1][col]
                next_min1_c = col
            elif next_min2 is None or grid[n - 1][col] <= next_min2:
                next_min2 = grid[n - 1][col]
                next_min2_c = col
        
        # Fill the recursive cases
        for row in range(n - 2, -1, -1):
            # Minimum and Second Minimum Column Index of the current row
            min1_c = None
            min2_c = None

            # Minimum and Second Minimum Value of the current row
            min1 = None
            min2 = None

            for col in range(n):
                # Select minimum from valid cells of the next row
                if col != next_min1_c:
                    value = grid[row][col] + next_min1
                else:
                    value = grid[row][col] + next_min2
                
                # Save minimum and second minimum 
                if min1 is None or value <= min1:
                    min2 = min1
                    min2_c = min1_c
                    min1 = value
                    min1_c = col
                elif min2 is None or value <= min2:
                    min2 = value
                    min2_c = col
            
            # Change of row. Update next_min1_c, next_min2_c, next_min1, next_min2
            next_min1_c = min1_c
            next_min2_c = min2_c
            next_min1 = min1
            next_min2 = min2
        
        # Return the minimum from the first row
        return next_min1
                

        
# @lc code=end

