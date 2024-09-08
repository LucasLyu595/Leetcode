#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, curr = 0, head
        while curr:
            curr = curr.next
            length += 1

        sizes, rm = [length // k] * k, length % k
        for i in range(rm):
            sizes[i] += 1

        res = []
        curr = head
        for size in sizes:
            if not size:
                res.append(None)
                continue
            res.append(curr)
            for i in range(size-1):
                curr = curr.next
            curr.next, curr = None, curr.next
        return res


# @lc code=end

