class Solution:
    """
    Optimised: O(N)
    """
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        break_count = 0

        for i in range(n):
            next_index = (i + 1) % n
            if nums[i] > nums[next_index]:
                break_count += 1
            
            if break_count > 1:
                return False

        return True


"""
Brute Force: O(N ^ 2)
"""
class Solution1:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        sorted_nums = sorted(nums)

        for i in range(n):
            rotated_version = sorted_nums[i:] + sorted_nums[:i]
            if rotated_version == nums:
                return True

        return False



    
        

        