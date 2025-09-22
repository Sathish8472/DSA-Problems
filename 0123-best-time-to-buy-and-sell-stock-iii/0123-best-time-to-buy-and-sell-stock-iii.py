class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n)]
        
        return self.solve(0, 0, 2, prices, dp, n)

    def solve(self, ind: int, holding: int, cap: int, prices: List[int], dp, n: int) -> int:
        if ind == n or cap == 0:
            return 0
        
        if dp[ind][holding][cap] != -1:
            return dp[ind][holding][cap]
        
        if holding == 0:
            take = -prices[ind] + self.solve(ind + 1, 1, cap, prices, dp, n)
            skip = self.solve(ind + 1, 0, cap, prices, dp, n)
            profit = max(take, skip)
        
        else:
            sell = prices[ind] + self.solve(ind + 1, 0, cap - 1, prices, dp, n)
            skip = self.solve(ind + 1, 1, cap, prices, dp, n)
            profit = max(sell, skip)
        
        dp[ind][holding][cap] = profit
        return profit