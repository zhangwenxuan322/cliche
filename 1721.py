# 1721. Swapping Nodes in a Linked List

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Solution of just swap value
        # first = last = head
        # for i in range(1, k):
        #     first = first.next
        #
        # null_checker = first
        # while null_checker.next:
        #     last = last.next
        #     null_checker = null_checker.next
        # first.val, last.val = last.val, first.val
        # return head
        node_list = []
        this = head
        while True:
            if this is not None:
                node_list.append(this.val)
                this = this.next
            else:
                break
        tmp = node_list[k - 1]
        node_list[k - 1] = node_list[len(node_list) - k]
        node_list[len(node_list) - k] = tmp
        node_tmp = None
        res_head = None
        for v in reversed(node_list):
            node = ListNode(v, node_tmp)
            node_tmp = node
            res_head = node

        return res_head

    def test(self):
        h5 = ListNode(5)
        h4 = ListNode(4, h5)
        h3 = ListNode(3, h4)
        h2 = ListNode(2, h3)
        head1 = ListNode(1, h2)
        res1 = self.swapNodes(head1, 2)
        while res1 is not None:
            print(res1.val)
            res1 = res1.next


Solution().test()
