class Solution:

    # Bitwise AND
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += n & 1  # Check last bit
            n >>= 1  # Right Shift

        return count

    # Time: O(Log N), Space: O(1)
    def hammingWeight_1(self, n: int) -> int:

        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n // 2  # O(log N)

        return count
