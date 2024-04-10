#
# @lc app=leetcode id=950 lang=python3
#
# [950] Reveal Cards In Increasing Order
#

# @lc code=start
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        dq=collections.deque()
        for card in reversed(sorted(deck)):
            dq.rotate()
            dq.appendleft(card)
        return dq

        
# @lc code=end

