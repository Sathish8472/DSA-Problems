class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) 

        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1