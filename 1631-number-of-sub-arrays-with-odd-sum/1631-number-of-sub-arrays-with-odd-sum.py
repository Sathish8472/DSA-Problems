class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        odd_count = 0
        even_count = 1
        current_sum = 0
        count = 0

        for num in arr:
            current_sum += num
            if current_sum % 2 == 0:
                count += odd_count
                even_count +=1 
            else:
                count += even_count
                odd_count += 1
            
            count %= MOD
        
        return count


    # Backtracking, NOT Efficient
    # Time: O(N ^ 3), Space: O(N)
    def numOfSubarrays1(self, arr: List[int]) -> int:
        count = 0

        def backtrack(start):
            nonlocal count
            for end in range(start, len(arr)):
                current_sum = sum(arr[start:end + 1])
                if current_sum % 2 != 0:
                    count += 1

        for i in range(len(arr)):
            backtrack(i)

        return count
