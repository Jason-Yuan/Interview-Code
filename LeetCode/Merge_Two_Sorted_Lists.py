# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        current = dummyHead
        while l1 and l2:
            if l1.val >= l2.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            current = current.next
        while l1:
            current.next = l1
            l1 = l1.next
            current = current.next
        while l2:
            current.next = l2
            l2 = l2.next
            current = current.next
        current.next = None
        return dummyHead.next