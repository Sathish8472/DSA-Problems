class Solution:
    # In-Place Reversal Efficient
    def rotated(self, nums: List[int], k: int) -> None:
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
    def rotate_2(self, nums: list[int], k: int) -> None:
        d = deque(nums)             # Extra space for deque
        d.rotate(k)                 
        for i in range(len(nums)):
            nums[i] = d[i]



    # Array Slicing 
    # Extra space - O(N)
    def rotate1(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums[:] = nums[-k:] + nums[:-k]      # Modify in-place



        