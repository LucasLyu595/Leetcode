#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry, tmp = divmod(l1.val + l2.val, 10)
        head = ListNode(tmp)
        l1, l2 = l1.next, l2.next
        cur = head
        while l1 and l2:
            carry, tmp = divmod(l1.val + l2.val + carry, 10)
            cur.next = ListNode(tmp)
            l1, l2 = l1.next, l2.next
            cur = cur.next
        l = l1 if l1 else l2
        while carry and l:
            carry, tmp = divmod(l.val + carry, 10)
            cur.next = ListNode(tmp)
            l = l.next
            cur = cur.next
        if l:
            cur.next = l
        if carry:
            cur.next = ListNode(carry)
        return head


        
# @lc code=end

