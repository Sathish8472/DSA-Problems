class Solution:
    # Optimized Approach (Using Dynamic Programming + HashMap)
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        index_map = {num: i for i, num in enumerate(arr)}
        dp = {}
        max_len = 0

        for j in range(n):
            for i in range(j):
                x = arr[j] - arr[i]
                if x < arr[i] and x in index_map:
                    k = index_map[x]
                    dp[i, j] = dp.get((k, i), 2) + 1
                    max_len = max(max_len, dp[i, j])
                
            
        return max_len if max_len >=3 else 0



    # Backtracking, Not EFficient
    def lenLongestFibSubseq_1(self, arr: List[int]) -> int:
        if not arr:
            return 0

        n = len(arr)
        long_len = 0

        def backtrack(index, sequence):
            nonlocal long_len

            if len(sequence) > 2:
                long_len = max(long_len, len(sequence))

            for i in range(index, n):
                if len(sequence) < 2 or (sequence[-2] + sequence[-1] == arr[i]):
                    backtrack(i + 1, sequence + [arr[i]])

        for i in range(n):
            backtrack(i + 1, [arr[i]])

        return long_len if long_len >= 3 else 0
