class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes)
        temp = []

        for i in range(len(boxes)):
            if boxes[i] == '1':
                temp.append(i)
            
        print("temp: ", temp)

        for i in range(len(boxes)):
            operations = 0
            for j in temp:
                if i != j:
                # print(f"i: {i}, j: {j}")
                    operations += abs(i - j)
            
            answer[i] = operations

        return answer