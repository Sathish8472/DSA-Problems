class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        # Keep checking bits until all numbers become 0
        while a > 0 or b > 0 or c > 0:

            # Get the last bit (rightmost) of a, b, and c
            last_bit_a = a % 2
            last_bit_b = b % 2
            last_bit_c = c % 2

            if last_bit_c == 1:
                # If c's bit is 1, at least one of a or b must be 1
                if last_bit_a == 0 and last_bit_b == 0:
                    flips += 1
            else:
                # If c's bit is 0, both a and b must be 0
                if last_bit_a == 1:
                    flips += 1
                
                if last_bit_b == 1:
                    flips += 1

            # Move to the next bit (right shift)  
            a >>= 1
            b >>= 1
            c >>= 1
        
        return flips