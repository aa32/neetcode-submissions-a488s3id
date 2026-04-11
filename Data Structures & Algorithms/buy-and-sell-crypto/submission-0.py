


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit =0
        
        min_val = prices[0]

        for i in range(1,len(prices)):
            if prices[i]< min_val:
                min_val = prices[i]
            elif prices[i]> min_val:
                profit = prices[i]-min_val
                max_profit = max(max_profit,profit)
            else:
                continue

        return max_profit





        
        