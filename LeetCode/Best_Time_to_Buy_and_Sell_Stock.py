class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        res = - sys.maxint
        end = 0
        minStart = prices[0]
        for i in range(1, len(prices)):
            end = prices[i]
            res = max(res, end - minStart)
            minStart = min(minStart, end)

        return 0 if res < 0 else res