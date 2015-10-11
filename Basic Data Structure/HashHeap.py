##############################################################################################################################
#      Project:                  Hash Max Heap
#      Info:                     1. Hash Max Heap is implemented based on max heap and hash map
#                                2. A heap data structure is a array which visualized as NEARLY completed binary tree
#                                3. NEARLY - because the outer(last) layer may not be completed
#                                4. Two types of heap: MinHeap and MaxHeap
#                                5. With hash map, the delete function can be O(logn) since find element will be O(1)
##############################################################################################################################

class node:
    """
    create a node class to handle the duplicates in heap.
    id => the index of x, num = number of x in heap
    """
    def __init__(self, id, number):
        self.id = id
        self.num = number

class HashHeap:
    def __init__(self):
        self.map = {}
        self.hashmaxheap = [0]
        self.map[0] = node(0, 1)
        self.currentSize = 0

    def put(self, data):
        """add a new item to the hashmaxheap"""
        if data in self.map:
            existData = self.map[data]
            self.map[data] = node(existData.id, existData.num + 1)
            self.currentSize += 1
            return 
        else:
            self.hashmaxheap.append(data)
            self.map[data] = node(len(self.hashmaxheap) - 1, 1)
            self.currentSize += 1
            self.siftUp(len(self.hashmaxheap) - 1)

    def peek(self):
        """returns the item with the maxmum key value"""
        return self.hashmaxheap[1]

    def get(self):
        """returns the item with the maxmum key value, removing the item from the heap"""
        res = self.hashmaxheap[1]
        if self.map[res].num == 1:
            if self.map[res].id == len(self.hashmaxheap) - 1:
                del self.map[res]
                self.hashmaxheap.pop()
                self.currentSize -= 1
                return res
            del self.map[res]
            self.hashmaxheap[1] = self.hashmaxheap[-1]
            self.map[self.hashmaxheap[1]] = node(1, self.map[self.hashmaxheap[1]].num)
            self.hashmaxheap.pop()
            self.siftDown(1)
        else:
            self.map[res] = node(1, self.map[res].num - 1)
        self.currentSize -= 1
        return res

    def delete(self, data):
        existData = self.map[data]
        if existData.num == 1:
            del self.map[data]
            if existData.id == len(self.hashmaxheap) - 1:
                self.hashmaxheap.pop()
                self.currentSize -= 1
                return
            self.hashmaxheap[existData.id] = self.hashmaxheap[-1]
            self.map[self.hashmaxheap[-1]] = node(existData.id, self.map[self.hashmaxheap[-1]].num)
            self.hashmaxheap.pop()
            self.siftUp(existData.id)
            self.siftDown(existData.id)
        else:
            self.map[data] = node(existData.id, existData.num - 1)
        self.currentSize -= 1

    def siftUp(self, index):
        # // means devide by 2 and return int
        while index // 2 > 0:
            if self.hashmaxheap[index] < self.hashmaxheap[index // 2]:
                break
            else:
                numA = self.map[self.hashmaxheap[index]].num
                numB = self.map[self.hashmaxheap[index // 2]].num
                self.map[self.hashmaxheap[index]] = node(index // 2, numA)
                self.map[self.hashmaxheap[index // 2]] = node(index, numB)
                self.hashmaxheap[index], self.hashmaxheap[index // 2] = self.hashmaxheap[index // 2], self.hashmaxheap[index] 
            index = index // 2

    def siftDown(self, index):
        """correct single violation in a sub-tree"""
        if index > (len(self.hashmaxheap) - 1) // 2:
            return
        # find the max child of current index
        if (index * 2 + 1) > (len(self.hashmaxheap) - 1) or self.hashmaxheap[index * 2] > self.hashmaxheap[index * 2 + 1]:
            maxChild = index * 2
        else:
            maxChild = index * 2 + 1
        if self.hashmaxheap[index] > self.hashmaxheap[maxChild]:
            return
        else:
            numA = self.map[self.hashmaxheap[index]].num
            numB = self.map[self.hashmaxheap[maxChild]].num
            self.map[self.hashmaxheap[index]] = node(maxChild, numA)
            self.map[self.hashmaxheap[maxChild]] = node(index, numB)
            self.hashmaxheap[index], self.hashmaxheap[maxChild] = self.hashmaxheap[maxChild], self.hashmaxheap[index] 
        self.siftDown(index * 2)
        self.siftDown(index * 2 + 1)

    def size(self):
        return self.currentSize

    def isEmpty(self):
        return self.currentSize == 0