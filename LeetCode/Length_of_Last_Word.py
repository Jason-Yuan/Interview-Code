class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if s == "":
            return 0
        Words = s.split(" ")
        for i in range(len(Words) - 1, -1, -1):
        	if len(Words[i]) != 0:
        		return len(Words[i])
        return 0