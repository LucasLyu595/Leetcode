#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = sorted(score, key=lambda x: -x)
        placement = {}
        for index, value in enumerate(rank):
            placement[value] = index
        ans = []
        for s in score:
            if placement[s] == 0:
                ans.append("Gold Medal")
            elif placement[s] == 1:
                ans.append("Silver Medal")
            elif placement[s] == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(f"{placement[s] + 1}")
        return ans
        
# @lc code=end

