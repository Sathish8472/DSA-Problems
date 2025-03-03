class Solution:

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [0] * len(nums)
        less_i = 0
        greater_i = len(nums) - 1

        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                ans[less_i] = nums[i]
                less_i += 1
            if nums[j] > pivot:
                ans[greater_i] = nums[j]
                greater_i -= 1

        while less_i <= greater_i:
            ans[less_i] = pivot
            less_i += 1

        return ans

    # Optimal: In-Place Dutch National Flag
    def pivotArray_4(self, nums: List[int], pivot: int) -> List[int]:
        arr = nums[:]
        n = len(nums)
        low, high = 0, n - 1

        for i in range(n):
            if arr[i] < pivot:
                arr[i], arr[low] = arr[low], arr[i]
                low += 1
            
        for i in range(n - 1, -1, -1):
            if arr[i] > pivot:
                arr[i], arr[high] = arr[high], arr[i]
                high -= 1
            
        return arr


    # Dutch National Flag Variation (Two Pointers)
    def pivotArray_3(self, nums: list[int], pivot: int) -> List[int]:
        left, right = [], []
        count = 0  # Count occurrences of pivot

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                count += 1  # Keep count of pivot elements

        return left + [pivot] * count + right

    # In-Place Partitioning (Two-Pass)
    # Extra Space
    def pivotArray_2(self, nums: list[int], pivot: int) -> List[int]:
        result = [0] * len(nums)
        index = 0

        for num in nums:
            if num < pivot:
                result[index] = num
                index += 1

        for num in nums:
            if num == pivot:
                result[index] = num
                index += 1

        for num in nums:
            if num > pivot:
                result[index] = num
                index += 1

        return result

    # Using Three Separate Lists
    # Extra Space
    def pivotArray_1(self, nums: List[int], pivot: int) -> List[int]:

        if not nums:
            return []

        less, equal, greater = [], [], []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)

        return less + equal + greater
