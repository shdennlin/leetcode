from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def mergeTwoLists(self, l1: Optional[ListNode],
    #                   l2: Optional[ListNode]) -> Optional[ListNode]:

    #     if not l1 or not l2:
    #         return l1 if l1 else l2

    #     dummy = ListNode(None)
    #     curr = dummy

    #     while l1 and l2:
    #         if l1.val <= l2.val:
    #             curr.next = l1
    #             curr = curr.next
    #             l1 = l1.next
    #         elif l1.val >= l2.val:
    #             curr.next = l2
    #             curr = curr.next
    #             l2 = l2.next

    #     if l1 == None:
    #         curr.next = l2
    #     elif l2 == None:
    #         curr.next = l1

    #     return dummy.next

    def mergeTwoLists(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(None)

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            elif l1.val >= l2.val:
                curr.next = l2
                curr = curr.next
                l2 = l2.next

        curr.next = l1 or l2

        return dummy.next
