# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        
        for i in range(1, m):
            head = head.next
            
        premNode = head
        mNode = head.next
        nNode = mNode
        postnNode = mNode.next
        
        for i in range(m, n):
            temp = postnNode.next
            postnNode.next = nNode
            nNode = postnNode
            postnNode = temp
            
        mNode.next = postnNode
        premNode.next = nNode
        
        return dummy.next