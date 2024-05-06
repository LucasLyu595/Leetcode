#
# @lc app=leetcode id=2487 lang=python3
#
# [2487] Remove Nodes From Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        rev = None

        # reverse the list and store in temp rev
        while dummy:
            next_node = dummy.next
            dummy.next = rev
            rev = dummy
            dummy = next_node

        # iterate over reversed list
        dummy = rev
        head = None
        max_value = float("-inf")

        # Create new list
        while dummy:
            if dummy.val >= max_value:
                max_value = dummy.val

                # same logic as for reversing
                new_node = dummy.next
                dummy.next = head
                head = dummy
                dummy = new_node
            else:
                dummy = dummy.next

        return head

        


            
        
# @lc code=end

