class Solution:
    MOD = int(1e9 + 7)

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        result = []

        for i in range(32):
            if (n & (1 << i)) != 0:
                powers.append(1 << i)
            
        for start, end in queries:
            product = 1
            for i in range(start, end + 1):
                product = (product * powers[i]) % self.MOD
            
            result.append(product)
        
        return result

        