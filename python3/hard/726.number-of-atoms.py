#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#

# @lc code=start
from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counter = Counter()

        def findCloseParentheses(start: int, end: int) -> int:
            counter = 0
            while start < end:
                if '(' == formula[start]:
                    counter += 1
                elif ')' == formula[start]:
                    counter -= 1
                    if not counter:
                        return start
                start += 1
            return -1

        def helper(start: int, end: int, mult: int) -> None:
            name = []
            while start < end:
                # recursive
                if '(' == formula[start]: 
                    if name:
                        element = ''.join(name)
                        counter[element] += mult
                        name = []
                    next = findCloseParentheses(start, end)
                    local_mult = 0
                    cur = next + 1
                    if cur >= end or not formula[cur].isdigit():
                        local_mult = 1
                    else:
                        while cur < end and formula[cur].isdigit():
                            local_mult *= 10
                            local_mult += int(formula[cur])
                            cur += 1
                    helper(start+1, next, mult * local_mult)
                    start = cur
                    continue
                # normal
                if formula[start].islower():
                    name.append(formula[start])
                    start += 1
                    continue
                # new atomic element
                if formula[start].isupper():
                    if name:
                        element = ''.join(name)
                        counter[element] += mult
                        name = []
                    name.append(formula[start])
                    start += 1
                    continue
                local_mult = 0
                while start < end and formula[start].isdigit():
                    local_mult *= 10
                    local_mult += int(formula[start])
                    start += 1
                element = ''.join(name)
                name = []
                counter[element] += local_mult * mult
            if name:
                element = ''.join(name)
                counter[element] += mult

        helper(0, len(formula), 1)
        ans = []
        for key in sorted(counter.keys()):
            if counter[key] > 1:
                ans.append(key + str(counter[key]))
                continue
            ans.append(key)
        return ''.join(ans)



# @lc code=end

