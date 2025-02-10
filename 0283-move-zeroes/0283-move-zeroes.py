class Solution:
    # Optimized Solution
    def moveZeroes(self, nums: List[int]) -> None:

        next_non_zero_position = 0

        for current in range(len(nums)):
            if nums[current] != 0:
                nums[next_non_zero_position], nums[current] = (
                    nums[current],
                    nums[next_non_zero_position],
                )
                next_non_zero_position += 1

    # Brute force
    def moveZeroes_1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_count = 0

        for num in nums:
            if num != 0:
                nums[non_zero_count] = num
                non_zero_count += 1

        for i in range(non_zero_count, len(nums)):
            nums[i] = 0
