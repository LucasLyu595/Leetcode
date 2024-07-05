#
# @lc app=leetcode id=2058 lang=python3
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []
        i = 0
        cur = head
        diff_prev, diff_next = 0, 1
        while cur.next:
            diff_next = cur.val - cur.next.val
            if diff_prev * diff_next < 0:
                critical_points.append(i)
            diff_prev = diff_next
            i += 1
            cur = cur.next
        if not critical_points or len(critical_points) == 1:
            return [-1, -1]
        maxDis = critical_points[-1] - critical_points[0]
        minDis = maxDis
        for i in range(1, len(critical_points)):
            minDis = min(minDis, critical_points[i] - critical_points[i-1])
        return [minDis, maxDis]


        
# @lc code=end

