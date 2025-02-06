class Solution:

    # Two pointer technique(Efficient way)
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for num in nums:
            if num != val:
                nums[count] = num
                count += 1

        return count

    # Brute force
    # Additional space for New Array
    def removeElement_1(self, nums: List[int], val: int) -> int:
        new_nums = [num for num in nums if num != val]

        # change the values in nums
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]

        return len(new_nums)
