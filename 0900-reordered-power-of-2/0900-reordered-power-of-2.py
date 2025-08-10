class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def digit_count(x):
            # Convert number to string, sort digits, return as a list
            return sorted(str(x))

        target = digit_count(n)

        # Check all powers of 2 from 2^0 to 2^30
        for i in range(31):
            power = 1 << i  # This is 2^i
            if digit_count(power) == target:
                return True

        return False