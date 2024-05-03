#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if not version1:
            version1 = ''
        if not version2:
            version2 = ''
        list1 = version1.split('.',maxsplit=1)
        list2 = version2.split('.',maxsplit=1)
        int1 = int(list1[0]) if list1[0] else 0
        int2 = int(list2[0]) if list2[0] else 0
        if int1 < int2: return -1
        if int1 > int2: return 1
        if len(list1) == len(list2) == 1:
            return 0
        if len(list1) > len(list2):
            list2.append('')
        if len(list2) > len(list1):
            list1.append('')
        return self.compareVersion(list1[1], list2[1])



# @lc code=end

