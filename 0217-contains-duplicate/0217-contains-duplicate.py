class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashMap = []
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        
        return False

        # for num in nums:
        #     if num in hashMap:
        #         return True
        #     else:
        #         hashMap.append(num)

        # return False
