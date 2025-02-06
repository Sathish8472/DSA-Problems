class Solution:
    # In-Place Reversal Efficient
    def rotate45(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n          # Handle edge case

        def reverseArray(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverseArray(0, n - 1)
        reverseArray(0, k - 1)
        reverseArray(k, n - 1)



    # Deque Data Structure
    def rotate(self, nums: list[int], k: int) -> None:
        d = deque(nums)
        d.rotate(k)
        for i in range(len(nums)):
            nums[i] = d[i]


    # Array Slicing 
    # Extra space - rotated variable O(N)
    def rotate2(self, nums: list[int], k: int) -> None:
        n = len(nums)
        n = k % n

        rotated = nums[-k:] + nums[:-k]
        for i in range(n):
            nums[i] = rotated[i]



        