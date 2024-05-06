#
# @lc app=leetcode id=2487 lang=python3
#
# [2487] Remove Nodes From Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque



class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = deque()
        cur = head
        while cur:
            while nodes and nodes[-1].val < cur.val:
                nodes.pop()
            nodes.append(cur)
            cur = cur.next
        dummy = ListNode()
        prev = None
        while nodes:
            cur = nodes.popleft()
            if prev:
                prev.next = cur
            prev = cur
            if not dummy.next:
                dummy.next = cur
        return dummy.next

            
        
# @lc code=end

