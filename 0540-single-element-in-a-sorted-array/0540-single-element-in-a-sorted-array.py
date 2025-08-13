class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            # Ensure mid is even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid

        return nums[low]



    def singleNonDuplicate22(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]
        
        low, high = 1, n - 2
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                low = mid + 1
            else:
                high = mid - 1
        
        return -1

    def singleNonDuplicate_2(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for num in nums:
            ans ^= num
        
        return ans
    
    # Brute - T: O(N)
    def singleNonDuplicate1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        for i in range(n):
            if i == 0:
                if nums[i] != nums[i + 1]:
                    return nums[i]
            
            elif i == n - 1:
                if nums[i] != nums[i - 1]:
                    return nums[i]

            elif nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]

        

        