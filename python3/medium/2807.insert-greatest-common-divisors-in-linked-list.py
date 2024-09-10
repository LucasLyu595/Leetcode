#
# @lc app=leetcode id=2807 lang=python3
#
# [2807] Insert Greatest Common Divisors in Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            new_gcd = math.gcd(cur.val, cur.next.val)
            tmp = ListNode(new_gcd, cur.next)
            cur.next = tmp
            cur = tmp.next
        return head

        
# @lc code=end

