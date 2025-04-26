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

    # Optimal Approach
    # Time: O(2 ^ n), Space: O(N)
    def subsetXORSum2(self, nums: List[int]) -> int:
        self.total_xor_sum = 0
        self.dfs(nums, 0, 0)

        return self.total_xor_sum

    def dfs(self, nums: List[int], start_index, current_xor):

        if start_index == len(nums):
            self.total_xor_sum += current_xor
            return
        
        self.dfs(nums, start_index + 1, current_xor ^ nums[start_index])

        self.dfs(nums, start_index + 1, current_xor)






    # Brute
    # Time: O(2 ^ n * n), Space: O(N)
    def subsetXORSum_1(self, nums: List[int]) -> int:
        self.total_xor_sum = 0
        self._generate_subsets_and_calculate_xor_sum(nums, 0, [])

        return self.total_xor_sum
    
    def _calculate_subset_xor(self, subset: List[int]):

            xor_sum = 0
            for num in subset:
                xor_sum ^= num

            return xor_sum
        
    def _generate_subsets_and_calculate_xor_sum(self, nums: List[int], start_index: int, current_subset: List[int]) -> int:     

            self.total_xor_sum += self._calculate_subset_xor(current_subset)
            
            for i in range(start_index, len(nums)):
                current_subset.append(nums[i])
                self._generate_subsets_and_calculate_xor_sum(nums, i + 1, current_subset)
                current_subset.pop()