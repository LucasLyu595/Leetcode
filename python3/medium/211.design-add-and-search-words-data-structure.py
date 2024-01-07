#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        t = self.trie
        for c in word:
            if c not in t: t[c] = WordDictionary()
            t = t[c].trie
        t["\n"] = True
        

    def search(self, word: str) -> bool:
        t = self.trie
        for i in range(len(word) - 1):
            c = word[i]
            if c == '.':
                for child in t:
                    if child == "\n": continue
                    next = t[child]
                    if next.search(word[i+1:]): return True
                return False
            if c not in t: return False
            t = t[c].trie
        if word[-1] == '.':
            for child in t:
                if child == "\n": continue
                tmp = t[child].trie
                if "\n" in tmp: 
                    return True
            return False
        elif word[-1] not in t: 
            return False
        t = t[word[-1]].trie
        return "\n" in t


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

