# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# method 1
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        
        stack = []
        slow, fast = head, head
        while fast != None and fast.next != None:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        if fast == None:
            pass
        else:
            slow = slow.next
        
        while slow != None:
            cur = stack.pop()
            if slow.val != cur:
                return False
            slow = slow.next
            
        return True
        
# method 2
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        if fast == None:
            secHalf = self.reverse(slow)
        else:
            secHalf = self.reverse(slow.next)
        
        while secHalf != None:
            if secHalf.val != head.val:
                return False
            secHalf = secHalf.next
            head = head.next
            
        return True
    
    def reverse(self, head):
        if not head:
            return head
        
        prev = None
        while head != None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev