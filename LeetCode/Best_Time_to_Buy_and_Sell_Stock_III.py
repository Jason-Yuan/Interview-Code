class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
            
        size = len(prices)
        left, right = [0 for i in range(size)], [0 for i in range(size)]
        # DP from left to right;
        left[0] = 0
        minPrice = prices[0]
        for i in range(size):
            minPrice = min(prices[i], minPrice)
            left[i] = max(left[i - 1], prices[i] - minPrice)
        
        # DP from right to left;
        right[size - 1] = 0
        maxPrice = prices[size - 1]
        for i in range(size - 2, -1, -1):
            maxPrice = max(prices[i], maxPrice)
            right[i] = max(right[i + 1], maxPrice - prices[i])
        
        profit = -sys.maxint - 1
        for i in range(size):
            profit = max(left[i] + right[i], profit)
            
        return profit