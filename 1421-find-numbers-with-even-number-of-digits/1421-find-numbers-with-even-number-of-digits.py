class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        even_count = 0

        for num in nums:
            count = 0
            while num > 0:
                count += 1
                num = num // 10
            
            if count % 2 == 0:
                even_count += 1

        return even_count
        