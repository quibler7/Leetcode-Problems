class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, cheap = 0, prices[0]

        for i in range(1, len(prices)):
            if prices[i] < cheap:
                cheap = prices[i]
            
            curr_profit = prices[i]-cheap
            max_profit = max(max_profit, curr_profit)
        
        return max_profit
        