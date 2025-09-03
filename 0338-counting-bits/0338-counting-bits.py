class Solution:
    # Optimized DP with LSB Formula
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)
        
        return result


    # Bitwise Right Shift
    def countBits3(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for i in range(1, n + 1):
            if i & 1 == 0:
                result[i] = result[i >> 1]
            else:
                result[i] = result[i >> 1] + 1
            
        return result
    
    # Division 
    def countBits2(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for i in range(1, n + 1):
            if i & 1 == 0:
                result[i] = result[i // 2]
            else:
                result[i] = result[i // 2] + 1
            
        return result

    # Brute Force with Built-in Function - n Log n
    def countBits1(self, n: int) -> List[int]:
        result = []
        result.append(0)

        for i in range(1, n + 1):
            count = bin(i).count('1')
            result.append(count)
        
        return result
        