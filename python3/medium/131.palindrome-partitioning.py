#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def __init__(self):
        self.memory = {}
        
    def partition(self, s: str) -> List[List[str]]:
        if(s in self.memory):
            return self.memory[s]
        
        if(len(s) == 0):
             result = [[]]
        elif(len(s) == 1):
             result = [[s]]
        else:
            result = []
            for i in range(1, len(s) + 1):  
                left = []
                if(s[:i] == s[:i][::-1]):
                    left.append([s[:i]])
                else:
                    continue
                right = self.partition(s[i:])

                for l in left:
                    for r in right:
                        result.append(l + r)
        
        self.memory[s] = result
        return result
        


# @lc code=end

