class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = grid[0]
        n = grid[0][0]
        arr = []

        isElementEven = True
        for gd in grid:
            for g in gd:
                if g % 2 != 0:
                    isElementEven = False
                arr.append(g)
            
        arr.sort()
        middle_element = arr[len(arr) // 2]
        
        # isEven = False
        # if x % 2 == 0:
        #     isEven = True
        # else:
        #     isEven = False
        
        # if isEven and isElementEven:
        #     print("eve Proceed")
        # elif not isEven and not isElementEven:
        #     print("od proceed")
        # else:
        #     print("not proceed")
        #     return -1

        # print(middle_element)
        # print(arr)

        operation_count = 0
        for num in arr:
            if num % x != middle_element % x:
                return -1
            
            operation_count += abs(middle_element - num) // x

            # while num != middle_element:
            #     if num > middle_element:
            #         num -= x
            #         operation_count += 1
            #     else:
            #         num += x
            #         operation_count += 1

        print(operation_count)

        return operation_count