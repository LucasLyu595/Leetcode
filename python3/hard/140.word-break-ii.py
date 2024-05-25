#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memoization = {}

        # Depth-first search function to find all possible word break combinations
        def dfs(start: int) -> List[str]:
            n = len(s)
            remaining_str = s[start:n]
            # Check if result for this substring is already memoized
            if remaining_str in memoization:
                return memoization[remaining_str]
            # Base case: when the string is empty, return a list containing an empty string
            if not remaining_str:
                return [""]
            results = []
            for i in range(start, n):
                current_word = s[start: i+1]
                # If the current substring is a valid word
                if current_word in word_set:
                    for next_word in dfs(i+1): # Append current word and next word with space in between if next word exists
                        results.append(
                            current_word + (" " if next_word else "") + next_word
                        )
            # Memoize the results for the current substring
            memoization[remaining_str] = results
            return results

        return dfs(0)


# @lc code=end

