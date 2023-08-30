#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, node, map, visited) -> None:
        if node in visited:
            return
        visited.add(node)
        if node not in map:
            map[node] = Node(node.val)
        for neighbor in node.neighbors:
            if neighbor not in map:
                map[neighbor] = Node(neighbor.val)
            map[node].neighbors.append(map[neighbor])
            self.dfs(neighbor, map, visited)
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        map, visited = dict(), set()
        self.dfs(node, map, visited)
        return map[node]
        
# @lc code=end

