class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = grid[0]
        n = grid[0][0]
        arr = [num for row in grid for num in row]

        remainder = arr[0] % x
        if any(num % x != remainder for num in arr):
            return -1

        arr.sort()
        median = arr[len(arr) // 2]
        
        operation_count = 0
        for num in arr:
            operation_count += abs(median - num) // x

        return operation_count