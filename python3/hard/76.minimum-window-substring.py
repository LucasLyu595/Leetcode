#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        if m < len(t): return ""
        dict_t = Counter(t)
        num_letter, fulfilled = len(dict_t), 0
        dict_s = defaultdict(int)
        res = ""
        left, right = 0, 0
        queue = deque()
        while right < m:
            while fulfilled < num_letter:
                if right >= m:
                    return res
                char = s[right]
                if char in dict_t:
                    dict_s[char] += 1
                    queue.append((char, right))
                    if dict_s[char] == dict_t[char]:
                        fulfilled += 1
                right += 1
            if not queue:
                left = right
            else:
                while True:
                    char = queue[0][0]
                    if dict_s[char] == dict_t[char]:
                        break
                    if dict_s[char] > dict_t[char]:
                        queue.popleft()
                        dict_s[char] -= 1
                left = queue[0][1]
            if not res or right - left < len(res):
                res = s[left:right]
            while fulfilled == num_letter:
                char, _ = queue.popleft()
                dict_s[char] -= 1
                if dict_s[char] < dict_t[char]:
                    fulfilled -= 1
        return res

            
        
# @lc code=end

