# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA, currB = headA, headB

        while currA != currB:
            currB = headA if currB is None else currB.next
            currA = headB if currA is None else currA.next

        return currA
