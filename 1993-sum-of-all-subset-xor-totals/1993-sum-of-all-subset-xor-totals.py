class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        sum_val = 0
        n = len(nums)

        def XORSum(arr):
            val = 0
            for num in arr:
                val ^= num

            return val


        def backtrack(start, ds):
            nonlocal sum_val

            sum_val += XORSum(ds)

            for i in range(start, n):
                ds.append(nums[i])

                backtrack(i + 1, ds)
                ds.pop()
                
        backtrack(0, [])

        return sum_val        