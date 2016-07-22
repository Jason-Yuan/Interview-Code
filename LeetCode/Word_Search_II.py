class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.IsWord = False
        

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.IsWord = True
        
class Solution(object):
    def __init__(self):
        self.result = []
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        for row_num in range(len(board)):
            for col_num in range(len(board[0])):
                self.search(board, row_num, col_num, trie.root, "")
                
        return self.result
                
    def search(self, board, x, y, cur_node, word):
        if cur_node.IsWord:
            self.result.append(word)
            cur_node.IsWord = False
        
        if not (x < 0 or x >= len(board) or y < 0 or y >= len(board[0])):
            temp = board[x][y]
            cur_node = cur_node.children.get(temp)
            if cur_node:
                board[x][y] = "#"
                self.search(board, x+1, y, cur_node, word+temp)
                self.search(board, x-1, y, cur_node, word+temp)
                self.search(board, x, y+1, cur_node, word+temp)
                self.search(board, x, y-1, cur_node, word+temp)
                board[x][y] = temp