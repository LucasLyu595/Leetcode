#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = collections.Counter(nums1) & collections.Counter(nums2)
        res = []

        for k, v in counts.items():
            res.extend([k] * v)
        
        return res
        
# @lc code=end

