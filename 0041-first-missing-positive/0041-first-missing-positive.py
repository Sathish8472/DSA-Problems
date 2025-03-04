class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False] * (n + 1)

        for num in nums:
            if 0 < num <= n:
                seen[num] = True

        for i in range(1, n + 1):
            if not seen[i]:
                return i

        return n + 1



    
    # Hashing Approach
    # Extra Space
    def firstMissingPositive_2(self, nums: List[int]) -> int:
        num_set = set(nums)
        expected = 1

        while expected in num_set:
            expected += 1
        return expected

        

    # Brute force
    # Sorting Approach (Not Optimal for Large Arrays)
    def firstMissingPositive_1(self, nums: List[int]) -> int:
        nums.sort()
        expected = 1
        for num in nums:
            if num == expected:
                expected += 1           # Adding 1
        return expected
    


    def firstMissingPositive11(self, nums: List[int]) -> int:
        i = 1
        while True:
            if i not in nums:
                return i
            i +=1

