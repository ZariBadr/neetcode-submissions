class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = []
        for i in range(len(prices)):
            for j in range(len(prices)):
                if i < j and prices[j] - prices[i] > 0:
                    buy.append(prices[j] - prices[i])
        if len(buy) != 0:
            return max(buy)
        return 0



        
        