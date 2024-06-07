#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = []
        sentence = sentence.split()
        pref_map = {}
        for word in dictionary:
            cur = pref_map
            for char in word:
                if '*' in cur:
                    break
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            if cur:
                cur.clear()
            cur['*'] = ''

        for word in sentence:
            cur = pref_map
            tmp = []
            notAppend = True
            for char in word:
                if char not in cur:
                    ans.append(word)
                    notAppend = False
                    break
                cur = cur[char]
                tmp.append(char)
                if '*' in cur:
                    break
            if notAppend:
                ans.append(''.join(tmp))
        return ' '.join(ans)



        

        

        
# @lc code=end

