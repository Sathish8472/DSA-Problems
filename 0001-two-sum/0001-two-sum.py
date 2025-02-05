class Solution:
    # HashMap Optimal solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in hashMap:
                return [hashMap[compliment], i]
            hashMap[num] = i


    # Brute force, Time: O(N ^ 2)
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        
        