#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left, right = head, head
        while right and right.next:
            left = left.next
            right = right.next.next
        if right:
            left = left.next
        
        def reverse(head: Optional[ListNode]) -> ListNode:
            pre, cur = None, head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre
        
        right = reverse(left)
        left = head
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
# @lc code=end

