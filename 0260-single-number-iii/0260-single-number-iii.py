class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for num in nums:
            xor ^= num

        diff_bit = xor & -xor
        x, y = 0, 0

        for num in nums:
            if num & diff_bit:
                x ^= num
            else:
                y ^= num

        return [x, y]
        