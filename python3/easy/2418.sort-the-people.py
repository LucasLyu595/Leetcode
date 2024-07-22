#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#

# @lc code=start
from collections import defaultdict


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map = defaultdict(list)
        for name, height in zip(names, heights):
            map[name].append(height) 
        return sorted(names, key=lambda x: -map[x].pop())
        
# @lc code=end

