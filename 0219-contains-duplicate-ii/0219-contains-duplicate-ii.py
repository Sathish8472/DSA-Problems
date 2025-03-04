class Solution:

    # Sliding Window / Set
    # Time: O(N), space: O(k)
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numSet = set()

        for i, num in enumerate(nums):
            if num in numSet:
                return True
            numSet.add(num)

            if len(numSet) > k:
                numSet.remove(nums[i - k])

        return False

    # Hashing
    # time: O(N), space: O(N)
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        hashMap = {}

        for i, num in enumerate(nums):
            if num in hashMap and abs(i - hashMap[num]) <= k:
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
                    return True

        return False
