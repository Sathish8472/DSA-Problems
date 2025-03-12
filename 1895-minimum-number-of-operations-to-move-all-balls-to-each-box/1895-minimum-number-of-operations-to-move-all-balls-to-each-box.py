class Solution:
    def minOperations(self, boxes: str) -> List[int]:   
        n = len(boxes)
        answer = [0] * n
        ones_indices = [i for i in range(n) if boxes[i] == '1']

        for i in range(n):
            operations = 0
            for j in ones_indices:
                if i != j:
                    operations += abs(i - j)

            answer[i] = operations

        return answer
