#
# @lc app=leetcode id=1634 lang=python3
#
# [1634] Add Two Polynomials Represented as Linked Lists
#

# @lc code=start
# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        dummy = PolyNode()
        prev = dummy
        while poly1 and poly2:
            curr = None
            if poly1.power > poly2.power:
                curr = PolyNode(poly1.coefficient, poly1.power)
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                curr = PolyNode(poly2.coefficient, poly2.power)
                poly2 = poly2.next
            else:
                if not poly1.coefficient + poly2.coefficient:
                    poly1 = poly1.next
                    poly2 = poly2.next
                    continue
                curr = PolyNode(poly1.coefficient + poly2.coefficient, poly1.power)
                poly1 = poly1.next
                poly2 = poly2.next
            prev.next = curr
            prev = curr
        poly = poly1 if poly1 else poly2
        while poly:
            curr = PolyNode(poly.coefficient, poly.power)
            poly = poly.next
            prev.next = curr
            prev = curr
        return dummy.next

# @lc code=end

