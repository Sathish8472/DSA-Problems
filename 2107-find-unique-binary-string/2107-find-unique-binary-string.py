class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = self.func("", nums)
        return result
    
    def func(self, current_string, nums):
        if len(current_string) == len(nums[0]):
            if current_string not in nums:
                return current_string
            else:
                return None

        result = self.func(current_string + '0', nums)

        if result:
            return result

        result = self.func(current_string + '1', nums)

        if result:
            return result


        