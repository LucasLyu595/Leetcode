#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
from collections import Counter
from functools import reduce
import operator


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return reduce(operator.__and__, map(Counter, words)).elements()
        
        

        
# @lc code=end

