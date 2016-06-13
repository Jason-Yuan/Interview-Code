# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        Dummy = ListNode(0)
        head = Dummy
        while l1 != None and l2 != None:
            sum = (l1.val + l2.val + carry) % 10
            carry = 1 if (l1.val + l2.val + carry) > 9 else 0
            head.next = ListNode(sum)
            head = head.next
            l1 = l1.next
            l2 = l2.next
            
        while l1 != None:
            sum = (l1.val + carry) % 10
            carry = 1 if l1.val + carry > 9 else 0
            head.next = ListNode(sum)
            l1 = l1.next
            head = head.next
        
        while l2 != None:
            sum = (l2.val + carry) % 10
            carry = 1 if l2.val + carry > 9 else 0
            head.next = ListNode(sum)
            l2 = l2.next
            head = head.next
        
        if carry:
            head.next = ListNode(carry)
        
        return Dummy.next