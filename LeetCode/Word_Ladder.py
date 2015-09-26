import Queue
import string

class Solution(object):
    def getNextWord(self, word, dict):
        aToz = string.ascii_lowercase
        res = []
        for char in aToz:
            for j in range(len(word)):
                if word[j] == char:
                    continue
                newWord = word[:j] + char + word[j+1:]
                if newWord in dict:
                    res.append(newWord)
        return res
        
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if not wordList:
            return 0
            
        q = Queue.Queue()
        visited = set()
        q.put(beginWord)
        visited.add(beginWord)
        length = 1
        while not q.empty():
            length += 1
            size = q.qsize()
            for i in range(size):
                word = q.get()
                for nextWord in self.getNextWord(word, wordList):
                    if nextWord in visited:
                        continue
                    if nextWord == endWord:
                        return length
                    q.put(nextWord)
                    visited.add(nextWord)
        return 0