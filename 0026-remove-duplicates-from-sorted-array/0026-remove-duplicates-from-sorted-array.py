class Solution:
    def removeDuplicates_1(self, nums: List[int]) -> int:

        if not nums:
            return 0

        pointer = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[pointer] = nums[i]
                pointer += 1
                
        return pointer

    def removeDuplicates(self, nums: List[int]) -> int:

        unique_elements = []

        for num in range(len(nums)):
            if num not in unique_elements:
                unique_elements.append(num)

        return len(unique_elements) - 1
