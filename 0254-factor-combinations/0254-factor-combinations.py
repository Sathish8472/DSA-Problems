class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, target):
            if target == 1 and len(current) > 1:
                result.append(current[:])
                return
            
            for i in range(start, int(target ** 0.5) + 1):
                if target % i == 0:
                    current.append(i)
                    backtrack(i, current, target // i) 
                    current.pop()
            
            if target >= start:
                current.append(target)
                backtrack(target, current, 1)  # Reduce target to 1
                current.pop()

        backtrack(2, [], n)
        return result
        