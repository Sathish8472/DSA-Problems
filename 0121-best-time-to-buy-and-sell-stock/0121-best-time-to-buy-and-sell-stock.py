class Solution:

    # One pass Efficient Approach
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)
                
        return max_profit

    


    # DP, Not Efficient
    # Time : O(N)
    def maxProfit_33(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        dp = [0] * n
        min_price = prices[0]

        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - min_price)

        return dp[-1]







    # Brute force
    # Time: O(n ^ 2)
    def maxProfit_1(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                    max_profit = max(max_profit, profit)

        return max_profit
        