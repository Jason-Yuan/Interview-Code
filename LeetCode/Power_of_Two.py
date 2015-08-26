class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n < 1:
            return False
        elif n & (n-1) == 0:
            return True
        else:
            return False