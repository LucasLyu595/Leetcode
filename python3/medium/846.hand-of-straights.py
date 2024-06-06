#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        counter = Counter(hand)
        for key in sorted(counter.keys()):
            num = counter[key]
            if not num:
                continue
            for i in range(groupSize):
                if counter[key+i] < num:
                    return False
                counter[key+i] -= num
        return True


        
# @lc code=end

