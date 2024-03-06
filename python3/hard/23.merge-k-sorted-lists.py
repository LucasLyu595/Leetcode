#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None

        def merge2Lists(list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]) -> Optional[ListNode]:
            if not list1:
                return list2
            if not list2:
                return list1
            head = ListNode()
            cur = head
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            cur.next = list1 if list1 else list2
            return head.next
        
        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]

        
# @lc code=end

