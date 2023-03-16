#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        len_needle = len(needle)
        len_haystack = len(haystack)
        if len_needle > len_haystack:
            return -1
        for i in range(len_haystack - len_needle + 1):
            if haystack[i] == needle[0]:
                if haystack[i:i + len_needle] == needle:
                    return i
        return -1
        
# @lc code=end

