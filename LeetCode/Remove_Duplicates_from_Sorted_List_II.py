# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        
        while head.next != None and head.next.next != None:
            if head.next.val == head.next.next.val:
                temp = head.next.val
                while head.next != None and head.next.val == temp:
                    head.next = head.next.next
            else:
                head = head.next
                
        return dummy.next