#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        counter = [0]
        while len(counter) < num+1:
            counter.extend([i+1 for i in counter])
        return counter[:num+1]
        
# @lc code=end

