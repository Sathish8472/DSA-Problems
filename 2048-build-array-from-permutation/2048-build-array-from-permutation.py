class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] += n * (nums[nums[i]] % n)

        print(nums)
        for i in range(n):
            nums[i] //= n
        return nums


    def buildArray1(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [nums[nums[i]] for i in range(n)]

        return ans 







   
    def buildArray_2(self, nums: List[int]) -> List[int]:
        ans = []

        for ind in nums:
            ans.append(nums[ind])

        return ans
        