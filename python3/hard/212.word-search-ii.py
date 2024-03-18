#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word
            
        m, n = len(board), len(board[0])
        res = []

        def backtrace(row: int, col: int, parent: map) -> None:
            letter = board[row][col]
            current_node = parent[letter]

            word_matched = current_node.pop(WORD_KEY, False)
            if word_matched:
                res.append(word_matched)
            
            board[row][col] = '#'

            for row_offset, col_offset in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
                new_row, new_col = row + row_offset, col + col_offset
                if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                    continue
                if board[new_row][new_col] not in current_node:
                    continue
                backtrace(new_row, new_col, current_node)

            board[row][col] = letter

            if not current_node:
                parent.pop(letter)
        
        for row in range(m):
            for col in range(n):
                if board[row][col] in trie:
                    backtrace(row, col, trie)
        return res

        
# @lc code=end

