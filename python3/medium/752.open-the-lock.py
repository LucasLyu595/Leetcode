#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = {}
        source = '0000'
        if target == source:
            return 0
        numWheels = 4
        for node in deadends:
            if node == source:
                return -1
            visited[node] = -1

        def getNeighbor(node: str) -> List[str]:
            nonlocal numWheels
            ans = []
            for i in range(numWheels):
                tmp = node[:i] + str((int(node[i])+1) % 10) + node[i+1:]
                if tmp not in deadends:
                    ans.append(tmp)
                tmp = node[:i] + str((int(node[i])-1) % 10) + node[i+1:]
                if tmp not in deadends:
                    ans.append(tmp)
            return ans
        
        frontier = deque([source])
        visited[source] = 0
        while frontier:
            node = frontier.popleft()
            for neighbor in getNeighbor(node):
                if neighbor not in visited:
                    visited[neighbor] = visited[node] + 1
                    if neighbor == target:
                        return visited[target]
                    frontier.append(neighbor)
        return -1



        
# @lc code=end

