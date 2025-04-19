class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]

        return self.func(coins, n - 1, amount, dp)
    
    def func(self, arr, ind, T, dp):

        if ind == 0:
            return 1 if T % arr[0] == 0 else 0
        
        if dp[ind][T] != -1:
            return dp[ind][T]

        not_taken = self.func(arr, ind - 1, T, dp)

        taken = 0
        if arr[ind] <= T:
            taken = self.func(arr, ind, T - arr[ind], dp)
        
        dp[ind][T] = not_taken + taken

        return dp[ind][T]

        