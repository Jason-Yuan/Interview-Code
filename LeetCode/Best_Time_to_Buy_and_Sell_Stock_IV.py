class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0:
            return 0
            
        if k >= len(prices) / 2:
            profit = 0
            for i in range(1, len(prices)):
                diff = prices[i] - prices[i - 1]
                if diff > 0:
                    profit += diff
            return profit
            
        n = len(prices)
        mustSell = [[0 for i in range(k + 1)] for i in range(n + 1)]
        globalBest = [[0 for i in range(k + 1)] for i in range(n + 1)]
        
        mustSell[0][0] = globalBest[0][0] = 0
        for i in range(1, k + 1):
            mustSell[0][i] = globalBest[0][i] = 0
            
        for i in range(1, n):
            profit = prices[i] - prices[i - 1]
            mustSell[i][0] = 0
            for j in range(1, k + 1):
                mustSell[i][j] = max(globalBest[i - 1][j - 1] + profit, mustSell[i - 1][j] + profit)
                globalBest[i][j] = max(globalBest[i - 1][j], mustSell[i][j])
                
        return globalBest[n - 1][k]