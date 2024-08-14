#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#

# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def numValid(maxDis: int) -> int:
            left, cnt = 0, 0
            for right in range(len(nums)):
                while nums[left] + maxDis < nums[right]:
                    left += 1
                cnt += right - left
            return cnt

        low = 0
        high = nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            count = numValid(mid)

            if count < k:
                low = mid + 1
            else:
                high = mid

        return low

        
# @lc code=end

