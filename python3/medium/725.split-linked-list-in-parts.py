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
        tails = [None] * k
        i = 0
        cur = head
        while cur and i < k:
            tails[i] = cur
            i += 1
            cur = cur.next

        def nextX(node: Optional[ListNode], x: int) -> Optional[ListNode]:
            while node and x:
                node = node.next
                x -= 1
            if x:
                return None
            return node

        cur = nextX(tails[-1], k)
        while cur:
            tails[-1] = cur
            for i in range(k - 1):
                tails[i] = nextX(tails[i], i + 1)
            cur = nextX(tails[-1], k)
        cur = tails[-1]
        i = 0
        while cur and cur.next:
            for j in range(i, k):
                tails[j] = tails[j].next
            cur = tails[-1]
            i += 1
        ans = [head]
        for i in range(k - 1):
            if tails[i]:
                ans.append(tails[i].next)
                tails[i].next = None
            else:
                ans.append(None)
        return ans


# @lc code=end

