# 234. Palindrome Linked List

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        ptr = head
        while ptr != None:
            arr.append(ptr.val)
            ptr = ptr.next
        return arr == arr[::-1]
