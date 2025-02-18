class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # print(nums)

        def backtrack(index, ds):
            result.append(ds[:])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue

                ds.append(nums[i])
                backtrack(i + 1, ds)
                ds.pop()

        backtrack(0, [])
        return result
