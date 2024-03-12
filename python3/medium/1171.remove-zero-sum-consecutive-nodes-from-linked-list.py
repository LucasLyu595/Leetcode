#
# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prefix_sum_map = {0: dummy}
        p = head
        prefix_sum = 0
        while p:
            prefix_sum += p.val
            prefix_sum_map[prefix_sum] = p
            p = p.next
        prefix_sum = 0
        p = dummy
        while p:
            prefix_sum += p.val
            p.next = prefix_sum_map[prefix_sum].next
            p = p.next
        return dummy.next
        
        
# @lc code=end

