class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        n = len(nums)

        def backtrack(current_subset):
            if len(current_subset) == n:
                result.append(current_subset[:])
                return

            for num in nums:
                if num in current_subset:
                    continue

                current_subset.append(num)
                backtrack(current_subset)
                current_subset.pop()

        backtrack([])

        return result
        