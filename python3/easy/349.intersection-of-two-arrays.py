#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = collections.Counter(nums1) & collections.Counter(nums2)
        res = []

        for k, v in counts.items():
            res.extend([k])

        return res
        
# @lc code=end

