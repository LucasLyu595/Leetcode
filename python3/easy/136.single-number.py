#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
f = open("user.out", 'w')
for line in stdin:
    print(reduce(xor, map(int, line.rstrip()[1:-1].split(','))), file=f)
        
# @lc code=end

