class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        mn = int(-1e14)
        dp = [[[mn] * 3 for _ in range(k + 1)] for _ in range(n + 1)]

        def f(i: int, k_left: int, state: int) -> int:
            if i == n:
                return 0 if state == 0 else mn
                
            if dp[i][k_left][state] != mn:
                return dp[i][k_left][state]

            p = prices[i]
            profit = mn

            # 1) do nothing
            profit = max(profit, f(i + 1, k_left, state))

            if state == 0:
                # Try buying or selling (to start a new transaction)
                profit = max(profit, f(i + 1, k_left, 1) - p)
                profit = max(profit, f(i + 1, k_left, 2) + p)
            elif k_left > 0:
                if state == 1:
                    # Complete buy-sell
                    profit = max(profit, f(i + 1, k_left - 1, 0) + p)
                else:
                    # Complete sell-buy
                    profit = max(profit, f(i + 1, k_left - 1, 0) - p)

            dp[i][k_left][state] = profit
            return profit

        return f(0, k, 0)