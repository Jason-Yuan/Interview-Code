# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        Dummy = ListNode(0)
        Dummy.next = head
        
        slow, fast = Dummy, Dummy.next
        while fast != None and fast.next != None:
            temp = fast.next.next
            slow.next = fast.next
            fast.next.next = fast
            fast.next = temp
            
            slow = fast
            fast = fast.next
        
        return Dummy.next