class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] 

        def backtrack(index, path):
            result.append(path)

            for i in range(index, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return result

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current, index):
            result.append(current[:])

            for i in range(index, len(nums)):
                current.append(nums[i])
                backtrack(current, i + 1)
                current.pop()

        backtrack([], 0)
        return result
