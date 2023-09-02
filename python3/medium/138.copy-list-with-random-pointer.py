#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        cur = head
        map = dict()
        while cur:
            map[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.random:
                map[cur].random = map[cur.random]
            if cur.next:
                map[cur].next = map[cur.next]
            cur = cur.next
        return map[head]

        
# @lc code=end

