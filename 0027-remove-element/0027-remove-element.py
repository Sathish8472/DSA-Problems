class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = val
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != k:
                nums[pointer] = nums[i]
                pointer += 1

        print(nums)
        return pointer 
