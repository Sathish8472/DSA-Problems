class Solution:
    def removeElement_11(self, nums: List[int], val: int) -> int:
        unique_index = 0

        for i in range(0, len(nums) - 1):
            if nums[i] != val:
                nums[unique_index] = nums[i]
                unique_index += 1

        return unique_index

    # Brute force
    def removeElement(self, nums: List[int], val: int) -> int:
        new_nums = [num for num in nums if num != val]

        # change the values in nums
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]

        return len(new_nums)
