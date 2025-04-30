class Solution:

    def findNumbers(self, nums: List[int]) -> int:

        even_count = 0
        for num in nums:
            if (
                (num >= 10 and num <= 99)
                or (num >= 1000 and num <= 9999)
                or (num == 100000)
            ):
                even_count += 1

        return even_count

    def findNumbers_2(self, nums: List[int]) -> int:

        even_count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                even_count += 1

        return even_count

    def findNumbers1(self, nums: List[int]) -> int:

        even_count = 0

        for num in nums:
            count = 0
            while num > 0:
                count += 1
                num = num // 10

            if count % 2 == 0:
                even_count += 1

        return even_count
