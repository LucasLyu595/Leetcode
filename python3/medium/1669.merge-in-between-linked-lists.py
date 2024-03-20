#
# @lc app=leetcode id=1669 lang=python3
#
# [1669] Merge In Between Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        left, right = list1, list1
        for i in range(b+1):
            right = right.next
            i += 1
            if i > b-a+2:
                left = left.next
        tail, tail_next = list2, list2.next
        while tail_next:
            tail = tail.next
            tail_next = tail.next
        left.next = list2
        tail.next = right
        return list1
        
# @lc code=end

