class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        result = []
        nums = []
        for i in range(1, 10):
            nums.append(i)
        
        self.func(0, [], n, nums, k, result)

        return result

    def func(self, ind, current_sub, current_sum, nums, k, result):
        if len(current_sub) == k:
            if current_sum == 0:
                result.append(current_sub[:])
            return

        if current_sum < 0:
            return

        if ind == len(nums):
            return

        current_sub.append(nums[ind])
        take = self.func(ind + 1, current_sub, current_sum - nums[ind], nums, k, result)
        current_sub.pop()

        self.func(ind + 1, current_sub, current_sum, nums, k, result)
