# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法一 递归
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == [] or lists == [[]]:
            return None
        return self.helper(lists)
    
    def helper(self, lists):
        if len(lists) <= 1:
            return lists[0]
        left = self.helper(lists[:len(lists) / 2])
        right = self.helper(lists[len(lists) / 2:])
        return self.merge(left, right)
        
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

# 方法二 非递归
class Solution(object):
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
        
# 方法三 k个数的min heap
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node: 
                heap.append((node.val, node))
        heapq.heapify(heap)
        head = ListNode(0)
        curr = head
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next: 
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next