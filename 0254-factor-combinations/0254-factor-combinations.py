class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        if n == 1:
            return []

        nums = []
        for i in range(2, n):
            nums.append(i)

        result = []
        self._calculate_factors(0, nums, [], 1, n, result)
        return result

    def _calculate_factors(self, ind, nums, current_sub, factor, target, result):
        if factor == target:
            result.append(current_sub[:])
            return

        if factor > target:
            return

        if ind >= len(nums):
            return

        current_sub.append(nums[ind])
        self._calculate_factors(
            ind, nums, current_sub, factor * nums[ind], target, result
        )
        current_sub.pop()

        self._calculate_factors(ind + 1, nums, current_sub, factor, target, result)

        return
