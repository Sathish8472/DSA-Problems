class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        transformed_array = []
        
        for i in range(n):
            new_index = (i + nums[i]) % n
            transformed_array.append(nums[new_index])
        
        return transformed_array
