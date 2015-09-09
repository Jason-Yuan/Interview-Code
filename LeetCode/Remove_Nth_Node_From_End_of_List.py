# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow, fast = head, head
        for i in range(n):
            fast = fast.next
            
        if not fast:
            head = slow.next
        else:
            while fast.next != None:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
        
        return head