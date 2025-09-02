class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        count = (1 << n)

        for val in range(count):
            subset = []
            for i in range(n):
                if val & (1 << i):
                    subset.append(nums[i])
            result.append(subset)

        return result

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        self.func(0, nums, [], result)

        return result

    
    def func(self, ind, nums,current_arr, result):

        if ind == len(nums):
            result.append(current_arr[:])
            return

        current_arr.append(nums[ind])
        self.func(ind + 1, nums, current_arr, result)
        current_arr.pop()

        self.func(ind + 1, nums, current_arr, result)

        return