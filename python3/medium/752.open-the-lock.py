#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        if "0000" in (deadends := set(deadends)):
            return -1
        transitions = {str(i): (str((i + 1) % 10), str((i - 1) % 10)) for i in range(10)}
        start, end = {"0000"}, {target}
        deadends.add("0000")
        deadends.add(target)
        turns = 1
        while start and end:
            if len(start) > len(end):
                start, end = end, start
            temp = set()
            for state in start:
                for i in range(4):
                    for j in transitions[state[i]]:
                        new_state = state[:i] + j + state[i+1:]
                        if new_state in end:
                            return turns
                        if new_state not in deadends:
                            deadends.add(new_state)
                            temp.add(new_state)
            start = temp
            turns += 1
        return -1



        
# @lc code=end

