class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values for the first element
                        continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1

                    # **Skip all duplicate values for the second element**
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # **Skip all duplicate values for the third element**
                    while left < right and right + 1 < n and nums[right] == nums[right + 1]:
                        right -= 1

        return result

    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()

        for i in range(n):
            hashmap = set()
            for j in range(i + 1, n):
                num = -(nums[i] + nums[j])
                if num in hashmap:
                    triplet = tuple(sorted([nums[i], nums[j], num]))
                    result.add(triplet)
                hashmap.add(nums[j])

        return list(result)

    # Brute Force
    def threeSum_1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if i != j and i != k and j != k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            print(f"i: {i}, j: {j}, k: {k}")
                            triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                            result.add(triplet)

        return list(result)
