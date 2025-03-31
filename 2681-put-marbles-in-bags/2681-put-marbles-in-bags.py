class Solution:

    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 0 or k == 1:
            return 0

        pairSums = [weights[i] + weights[i + 1] for i in range(n - 1)]

        print("pairSum: ", pairSums)
        pairSums.sort()

        # Compute min and max partition scores using first k-1 and last k-1 elements
        min_score = sum(pairSums[:k - 1])
        max_score = sum(pairSums[-(k - 1):])

        return max_score - min_score


    # Brute force
    def putMarbles_1(self, weights: List[int], k: int) -> int:

        n = len(weights)
        result = []
        partition_min = float('inf')
        partition_max = 0

        def calculateSum(partitions):
            resultSum = 0
            print("part: ", partitions)
            for arr in partitions:
                pLen = len(arr)
                resultSum += (arr[0] + arr[pLen - 1])

            print("resultSum: ", resultSum)
            return resultSum

        def backtrack(start, partitions):
            nonlocal partition_min, partition_max
            if len(partitions) == k:
                if start == n:  
                    pSum = calculateSum(partitions)
                    if(pSum <= partition_min):
                        partition_min = pSum
                    
                    if(pSum >= partition_max):
                        partition_max = pSum 
                    print("psum: ", pSum)
                    result.append(partitions[:])
                return
            
            for end in range(start, n):
                backtrack(end + 1, partitions + [weights[start:end + 1]])

        backtrack(0, [])
        print(result)  # All possible valid p
        
        print("partition_max: ", partition_max, ", partition_min: ", partition_min)
        return partition_max - partition_min
        