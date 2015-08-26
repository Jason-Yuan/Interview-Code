class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        res = []
        self.parenthesesRecur(res, "", n, n)
        return res
        
        
    def parenthesesRecur(self, res, cur, left, right):
        if left == 0 and right == 0:
            res.append(cur)
            
        if left > 0:
            self.parenthesesRecur(res, cur + "(", left - 1, right)
            
        if right > left:
            self.parenthesesRecur(res, cur + ")", left, right - 1)