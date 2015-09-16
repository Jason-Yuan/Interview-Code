# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        return dummy.next
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        while len(lists) > 1:
            new_lists = []
            for i in range(0, len(lists) - 1, 2):
                merge_list = self.merge(lists[i], lists[i + 1])
                new_lists.append(merge_list)
            if len(lists) % 2 == 1:
                new_lists.append(lists[len(lists) - 1])
                
            lists = new_lists
        return lists[0]