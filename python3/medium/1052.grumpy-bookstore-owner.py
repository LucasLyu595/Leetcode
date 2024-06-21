#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        for i in range(len(customers)):
            if grumpy[i]:
                continue
            ans += customers[i]
            customers[i] = 0
        left = 0
        base = ans
        for right in range(len(customers)):
            base += customers[right]
            right += 1
            if right < minutes:
                continue
            elif right == minutes:
                ans = max(ans, base)
            else:
                base -= customers[left]
                ans = max(ans, base)
                left += 1
        ans = max(ans, base)
        return ans



# @lc code=end

