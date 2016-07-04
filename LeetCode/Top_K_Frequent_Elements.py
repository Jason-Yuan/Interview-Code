import Queue

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        
        minHeap = Queue.PriorityQueue()
        for key, count in map.items():
            if minHeap.qsize() < k:
                minHeap.put((count, key))
            elif minHeap.queue[0] < (count, key):
                minHeap.get()
                minHeap.put((count, key))
                
        return [x[1] for x in minHeap.queue]