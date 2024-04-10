#
# @lc app=leetcode id=950 lang=python3
#
# [950] Reveal Cards In Increasing Order
#

# @lc code=start
from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        sorted_deck = sorted(deck)
        ans = deque()
        while sorted_deck:
            if ans:
                tmp = ans.pop()
                ans.insert(0, tmp)
            card = sorted_deck.pop()
            ans.insert(0, card)
        return ans

        
# @lc code=end

