#
# @lc app=leetcode id=2181 lang=python3
#
# [2181] Merge Nodes in Between Zeros
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = ListNode(0, head), head.next
        sum = 0
        while fast:
            sum += fast.val
            if not fast.val:
                slow.next.val = sum
                sum = 0
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head


        
# @lc code=end

