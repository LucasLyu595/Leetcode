#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words[0]

        result = []
        chars = set(words[0])
        
        for char in chars:
            frequency = min([word.count(char) for word in words])
            result += frequency * [char]

        return result
        
        

        
# @lc code=end

