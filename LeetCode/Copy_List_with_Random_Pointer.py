# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyNext(self, head):
        while head != None:
            temp = RandomListNode(0)
            temp.label = head.label
            temp.random = head.random
            temp.next = head.next
            head.next = temp
            head = head.next.next
        
    def copyRandom(self, head):
        while head != None:
            if head.next.random != None:
                head.next.random = head.random.next
            head = head.next.next
        
    def splitList(self, head):
        newHead = head.next
        while head != None:
            temp = head.next
            head.next = temp.next
            head = head.next
            if temp.next != None:
                temp.next = temp.next.next
        return newHead
            
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
            
        self.copyNext(head)
        self.copyRandom(head)
        return self.splitList(head)