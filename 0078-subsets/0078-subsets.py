class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current, index):
            result.append(current[:])

            for i in range(index, len(nums)):
                current.append(nums[i])
                backtrack(current, i + 1)
                current.pop()

        backtrack([], 0)
        return result
        