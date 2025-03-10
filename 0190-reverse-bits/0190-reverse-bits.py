class Solution:

    # Bit Manipulation Approach
    # Time: O(1), SpacE: O(1)
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):         # Fixed iterations 32, So constant
            bit = n & 1
            result = (result << 1) | bit
            
            n >>= 1

        return result
        