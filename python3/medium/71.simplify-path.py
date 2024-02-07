#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        res = []
        for dir in dirs:
            if dir == '' or dir == '.':
                continue
            elif dir == "..":
                if len(res) != 0:
                    res.pop()
            else:
                res.append(dir)
        return "/" + "/".join(res)
        
# @lc code=end

