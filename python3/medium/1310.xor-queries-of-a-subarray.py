#
# @lc app=leetcode id=1310 lang=python3
#
# [1310] XOR Queries of a Subarray
#

# @lc code=start
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] ^ arr[i]
        ans = [0] * len(queries)
        for i, (left, right) in enumerate(queries):
            ans[i] = prefix[right]
            if left > 0:
                ans[i] ^= prefix[left - 1]
        return ans

# @lc code=end

