#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)

        def isPalindrome(start: int, end: int) -> bool:
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def backtrack(cur: list, start: int) -> None:
            if start == n:
                ans.append(cur)
                return
            for i in range(start, n):
                if isPalindrome(start, i):
                    backtrack(cur+[s[start:i+1]], i+1)
        backtrack([], 0)
        return ans 


# @lc code=end

