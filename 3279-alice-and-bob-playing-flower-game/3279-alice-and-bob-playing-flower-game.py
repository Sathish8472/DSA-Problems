class Solution:
    # Optimal
    def flowerGame(self, n: int, m: int) -> int:
        return (m * n) // 2

    # Optimal with why ??
    def flowerGame1(self, n: int, m: int) -> int:
        oddN, evenN = (n + 1) // 2, n // 2
        oddM, evenM = (m + 1) // 2, m // 2

        return oddN * evenM + evenN * oddM
    

# Optimized Solution (Formula)
# Instead of looping, just count odds and evens.

# In [1..n]
# Odd numbers = (n+1)//2
# Even numbers = n//2

# In [1..m]
# Odd numbers = (m+1)//2
# Even numbers = m//2

# Alice wins if:
# Lane1 is odd & Lane2 is even
# Lane1 is even & Lane2 is odd

# So: result = oddN * evenM + evenN * oddM


    # Brute 
    def flowerGame1(self, n: int, m: int) -> int:
        count = 0
        for x in range(1, n+1):
            for y in range(1, m+1):
                if (x + y) % 2 == 1: 
                    count += 1
        return count


