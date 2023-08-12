#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        oribin='{0:032b}'.format(n) # int -> string
        reversebin=oribin[::-1]
        return int(reversebin,2)
        
# @lc code=end

