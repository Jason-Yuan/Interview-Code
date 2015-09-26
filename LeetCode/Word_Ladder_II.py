import Queue

class Solution(object):
    def buildIndex(self, length, dict):
        indexes = []
        for i in range(length):
            index = {}
            for word in dict:
                entry = word[:i] + word[i + 1:]
                words = index.get(entry, [])
                words.append(word)
                index[entry] = words
            indexes.append(index)
        return indexes
     
    def getNextWord(self, word):
        res = []
        for i in range(len(word)):
            entry = word[:i] + word[i + 1:]
            if entry in self.indexes[i]:
                for nextWord in self.indexes[i][entry]:
                    if nextWord != word:
                        res.append(nextWord)
        return res
        
    def BFS(self, start, end):
        self.distance = {}
        self.distance[start] = 0
        q = Queue.Queue()
        q.put(start)
        while not q.empty():
            head = q.get()
            for nextWord in self.getNextWord(head):
                if nextWord not in self.distance:
                    self.distance[nextWord] = self.distance[head] + 1
                    q.put(nextWord)
    
    def DFS(self, current, target, path):
        if current == target:
            self.result.append(path[:])
            return
        
        for word in self.getNextWord(current):
            if self.distance[word] - 1 == self.distance[current]:
                self.DFS(word, target, path + [word])
        
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        if beginWord is None or endWord is None or len(beginWord) != len(endWord):
            return []
            
        if beginWord not in wordlist or endWord not in wordlist:
            return []
            
        self.indexes = self.buildIndex(len(beginWord), wordlist)
        self.BFS(beginWord, endWord)
        
        self.result = []
        if beginWord in self.distance:
            self.DFS(beginWord, endWord, [beginWord])
            
        return self.result