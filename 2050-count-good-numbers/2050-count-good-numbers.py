class Solution:
    def countGoodNumbers(self, n: int) -> int:

        MOD = 10 **9 + 7

        if n == 1:
            return 5

        num_even_pos = (n + 1) // 2
        num_odd_pos = n // 2

        count_even = pow(5, num_even_pos, MOD)
        count_odd = pow(4, num_odd_pos, MOD)

        result = (count_even * count_odd) % MOD
        
        return result

        