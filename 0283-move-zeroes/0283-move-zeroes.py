class Solution:
    # Optimal One-Pass Approach (Minimize Writes)
    def moveZeroes2(self, nums: List[int]) -> None:
        next_non_zero_position = 0  # Slow pointer

        for current in range(len(nums)):  # Fast pointer
            if nums[current] != 0:
                if current != next_non_zero_position:  # Avoid unnecessary swaps
                    nums[next_non_zero_position], nums[current] = (
                        nums[current],
                        nums[next_non_zero_position],
                    )
                next_non_zero_position += 1

    #  Two-Pass Approach (Faster but Extra Writes)
    def moveZeroes_1(self, nums: List[int]) -> None:
        non_zero_count = 0

        # First pass: Move non-zero elements forward
        for num in nums:
            if num != 0:
                nums[non_zero_count] = num
                non_zero_count += 1

        # Second pass: Fill remaining positions with zeros
        for i in range(non_zero_count, len(nums)):
            nums[i] = 0

    # Brute force
    def moveZeroes(self, nums: List[int]) -> None:
        temp = [num for num in nums if num != 0]  # Collect non-zero elements
        temp.extend([0] * (len(nums) - len(temp)))  # Append zeroes
        nums[:] = temp  # Copy back to original array
