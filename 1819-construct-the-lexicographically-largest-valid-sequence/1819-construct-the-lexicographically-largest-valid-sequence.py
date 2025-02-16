class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        sequence = [0] * size
        used = [False] * (n + 1)
        print(sequence)
        print(used)
        
        def backtrack(index):
            if index == size:  # Base case: all positions are filled
                return True
            
            if sequence[index] != 0:  # Skip already filled positions
                return backtrack(index + 1)
            
            # Try placing numbers from n to 1 (greedy approach)
            for num in range(n, 1, -1):
                if used[num]: 
                    continue
                if index + num < size and sequence[index] == 0 and sequence[index + num] == 0:
                    # Place the number
                    sequence[index] = sequence[index + num] = num
                    used[num] = True
                    
                    if backtrack(index + 1):  # Recursive step
                        return True
                    
                    # Backtrack if failed
                    sequence[index] = sequence[index + num] = 0
                    used[num] = False
            
            # Place 1 (it occurs only once)
            if not used[1]:
                sequence[index] = 1
                used[1] = True
                if backtrack(index + 1):
                    return True
                sequence[index] = 0
                used[1] = False
            
            return False

        backtrack(0)
        return sequence
