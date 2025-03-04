class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}

        for i, num in enumerate(nums):
            if num in hashMap:
                if abs(i - hashMap[num]) <= k:
                    return True

            hashMap[num] = i

        return False

    # Brute Approach
    # Time: O(N ^ 2)
    def containsNearbyDuplicate_1(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(n):
                if i != j and nums[i] == nums[j] and abs(j - i) <= k:
                    print(f"i:{i}, j:{j}")
                    return True

        return False



        