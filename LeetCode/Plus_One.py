class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == 1:
                digits[i] += 1
            if digits[i] > 9:
            	carry = 1
            else:
            	carry = 0
            digits[i] = digits[i] % 10
        if carry == 1:
            digits.insert(0, 1)
        
        return digits