class Solution:

    # Hashing / Hash Set approach
    # Time: O(N), Time: O(N)
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False

    # Sorting approach
    # Time: O(N Log N)
    def containsDuplicate_1(self, nums: List[int]) -> bool:
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
