class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        zero_count = nums.count(0)
        if zero_count == 0:
            return 0

        count = 0
        left = 0
        while left <= n - 3:
            if nums[left] == 0:
                for i in range(left, left + 3):
                    nums[i] ^= 1
                
                count += 1
            
            left += 1

        if n == sum(1 for num in nums if num == 1):
            return count

        return -1

    def minOperations2(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        left = 0
        right = left + 3

        while right <= n:
            if nums[left] == 0:
                count += 1
                nums[left] = 1
                if nums[left + 1] == 0:
                    nums[left + 1] = 1
                else:
                    nums[left + 1] = 0

                if nums[left + 2] == 0:
                    nums[left + 2] = 1
                else:
                    nums[left + 2] = 0

            left += 1
            right += 1

        if n == sum(1 for num in nums if num == 1):
            return count

        return -1

    def minOperations1(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        if n == sum(1 for num in nums if num == 1):
            return count

        for i in range(n):
            if n == sum(1 for num in nums if num == 1):
                return count
            if nums[i] == 0 and i + 3 <= n:
                for j in range(i, i + 3):
                    if nums[j] == 0:
                        nums[j] = 1
                    else:
                        nums[j] = 0
                count += 1

        if n == sum(1 for num in nums if num == 1):
            return count
        else:
            return -1
