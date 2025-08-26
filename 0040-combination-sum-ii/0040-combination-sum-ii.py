class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        self.func(0, target, [], candidates, ans)
        return ans

    def func(self, ind, current_sum, current_sub, nums, result):
        if current_sum < 0:
            return

        if current_sum == 0:
            result.append(current_sub[:])
            return

        if ind == len(nums):
            return

        current_sub.append(nums[ind])
        current_sum -= nums[ind]
        take = self.func(ind + 1, current_sum, current_sub, nums, result)
        current_sub.pop()
        current_sum += nums[ind]

        for i in range(ind + 1, len(nums)):
            if nums[i] != nums[ind]:
                self.func(i, current_sum, current_sub, nums, result)
                break
        return

    def combinationSum22(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(index, current, target):
            if target == 0:
                result.append(current[:])
                return

            for i in range(index, len(candidates)):
                candidate = candidates[i]

                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                if candidate > target:
                    break

                current.append(candidate)
                backtrack(i + 1, current, target - candidate)
                current.pop()

        backtrack(0, [], target)
        return result
