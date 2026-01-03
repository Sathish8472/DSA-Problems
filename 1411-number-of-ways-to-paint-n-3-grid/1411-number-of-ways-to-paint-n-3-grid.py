class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 12
        
        if n == 2:
            return 54
        
        diff, same = 6, 6

        for i in range(1, n):
            newDiff = (2 * diff + 2 * same) % MOD
            newSame = (2 * diff + 3 * same) % MOD

            diff, same = newDiff, newSame
        
        return (diff + same) % MOD