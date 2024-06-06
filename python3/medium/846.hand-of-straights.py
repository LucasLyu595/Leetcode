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
        m = len(counter.keys())
        for key in counter.keys():
            if not counter[key]:
                continue
            start = key
            while counter[start - 1]:
                start -= 1
            while start <= key:
                num = counter[start]
                if num:
                    for i in range(groupSize):
                        if counter[start+i] < num:
                            return False
                        counter[start+i] -= num
                start += 1
                m -= 1
                if not m:
                    return True
        return True



        
# @lc code=end

