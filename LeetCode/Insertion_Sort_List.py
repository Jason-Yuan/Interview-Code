# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        last = head.val
        while head.next != None:
            if head.next.val >= last:
                last = head.next.val
                head = head.next
            else:
                self.insert(dummy, ListNode(head.next.val))
                head.next = head.next.next
        return dummy.next
        
    def insert(self, head, node):
        while head.next != None and head.next.val <= node.val:
            head = head.next
        node.next = head.next
        head.next = node