#
# @lc app=leetcode id=2751 lang=python3
#
# [2751] Robot Collisions
#

# @lc code=start
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        line = list(range(n))
        line.sort(key=lambda x: positions[x])
        remainders = []
        for x in line:
            if 'R' == directions[x]:
                remainders.append(x)
            else:
                if not remainders:
                    remainders.append(x)
                    continue
                prev = remainders[-1]
                while -1 != prev and 'R' == directions[prev]:
                    if healths[prev] > healths[x]:
                        healths[prev] -= 1
                        break
                    if healths[prev] == healths[x]:
                        remainders.pop()
                        break
                    # health[prev] < health[x]
                    healths[x] -= 1
                    remainders.pop()
                    if not remainders:
                        prev = -1
                    else:
                        prev = remainders[-1]
                if -1 == prev or 'L' == directions[prev]:
                    remainders.append(x)
        remainders.sort()
        return [healths[x] for x in remainders if healths[x] != 0]

        
# @lc code=end

