class Solution:

    # Dutch National Flag Variation (Two Pointers)
    def pivotArray(self, nums: list[int], pivot: int) -> List[int]:
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
