#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def dfs(self, board: List[List[str]], i: int, j: int, word: str) -> bool:
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res


    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            j = 0
            start = 0
            while True:
                try:
                    j = board[i][start:].index(word[0])
                except ValueError:
                    break
                if self.dfs(board, i, start+j, word): return True
                start += j+1
        return False
        
# @lc code=end

