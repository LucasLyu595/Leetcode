#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        if n == 1:
            return res
        def getProduct(i:int, j:int) -> int:
            res = 1
            for x in range(i, j+1):
                res *= nums[x]
            return res
        def maxProductPartial(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            try:
                index = i+nums[i:j+1].index(0)
                tmp = [0]
                if i <= index-1:
                    tmp.append(maxProductPartial(i, index-1))
                if index+1 <= j:
                    tmp.append(maxProductPartial(index+1, j))
                return max(tmp)
            except ValueError:
                negative_indices = [index for index, value in enumerate(nums[i:j+1]) if value < 0]
                if len(negative_indices) % 2 == 0:
                    return getProduct(i, j)
                else:
                    return max(getProduct(i, i+negative_indices[-1]-1), getProduct(i+negative_indices[0]+1, j))
        return maxProductPartial(0, n - 1)


        
# @lc code=end

