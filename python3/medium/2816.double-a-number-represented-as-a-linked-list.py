#
# @lc app=leetcode id=2816 lang=python3
#
# [2816] Double a Number Represented as a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            prev, cur = None, head
            while cur:
                next = cur.next
                cur.next = prev
                prev, cur = cur, next
            return prev
        head = reverse(head)
        cur = head
        carry = 0
        while cur.next:
            cur.val = cur.val * 2 + carry
            carry = cur.val // 10
            cur.val = cur.val % 10
            cur = cur.next
        cur.val = cur.val * 2 + carry
        carry = cur.val // 10
        cur.val = cur.val % 10
        if carry:
            cur.next = ListNode(carry)
        return reverse(head)
        
        
# @lc code=end

