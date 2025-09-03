class Solution:
    def countBits(self, n: int) -> List[int]:

        result = []

        result.append(0)

        for i in range(1, n + 1):
            count = bin(i).count('1')
            result.append(count)
        
        return result
        