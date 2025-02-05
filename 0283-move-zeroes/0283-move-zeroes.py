class Solution: 
    # Optimized Solution
    def moveZeroes(self, nums: List[int]) -> None:

        last_non_zero_found = 0;
        
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[last_non_zero_found], nums[cur] = nums[cur], nums[last_non_zero_found]
                last_non_zero_found += 1



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
        