#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans = deque()
        for digit in num:
            tmp = int(digit)
            while ans and k and tmp < ans[-1]:
                ans.pop()
                k -= 1
            ans.append(tmp)
        while k and ans:
            ans.pop()
            k -= 1
        while ans and not ans[0]:
            ans.popleft()
        if not ans:
            return '0'
        return ''.join(str(digit) for digit in ans)
        

        
# @lc code=end

