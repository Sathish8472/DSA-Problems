class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.func(0, nums, [], result)

        return result

    
    def func(self, ind, nums, current_arr, result):
        if ind == len(nums):
            result.append(current_arr[:])
            return

        current_arr.append(nums[ind])
        self.func(ind + 1, nums, current_arr, result)
        current_arr.pop()

        for j in range(ind + 1, len(nums)):
            if nums[j] != nums[ind]:
                self.func(j, nums, current_arr, result)
                return

        self.func(len(nums), nums, current_arr, result)
            
        return
    
