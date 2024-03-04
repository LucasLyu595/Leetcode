#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        count = 0
        while count < n:
            end = end.next
            count += 1
        n, prev = head, None
        while end:
            end = end.next
            n, prev = n.next, n
        if not prev: return n.next
        prev.next = n.next
        return head
        
        
# @lc code=end

