class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        current_min=prices[0]
        for i in range(len(prices)):
            if prices[i] < current_min:
                current_min=prices[i]
            else:
                profit=max(profit, prices[i]-current_min)
            
        return profit
             
        