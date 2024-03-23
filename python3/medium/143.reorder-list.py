#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(head: Optional[ListNode]) -> ListNode:
            pre, cur = None, head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre
        
        tail = reverse(slow)
        dummy = ListNode(0, head)
        while head and tail:
            next = head.next
            head.next = tail
            head = next
            next = tail.next
            if tail == head:
                break
            tail.next = head
            tail = next
        return dummy.next

            
        
# @lc code=end

