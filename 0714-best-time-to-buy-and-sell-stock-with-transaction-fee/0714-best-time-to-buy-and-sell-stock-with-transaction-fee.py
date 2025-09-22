class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]

        return self.solve(0, 0, prices, fee, n, dp)
    
    def solve(self, ind: int, holding: int, prices: List[int], fee: int, n: int, dp) -> int:
        if ind == n:
            return 0
        
        if dp[ind][holding] != -1:
            return dp[ind][holding]
        
        if holding == 0:
            buy = -prices[ind] + self.solve(ind + 1, 1, prices, fee, n, dp)
            skip = 0 + self.solve(ind + 1, 0, prices, fee, n, dp)
            profit = max(buy, skip)
        else:
            sell = prices[ind] - fee + self.solve(ind + 1, 0, prices, fee, n, dp)
            skip = self.solve(ind + 1, 1, prices, fee, n, dp)

            profit = max(sell, skip)
        
        dp[ind][holding] = profit
        return profit
        
