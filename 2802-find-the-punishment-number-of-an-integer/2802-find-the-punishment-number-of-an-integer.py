class Solution:
    def punishmentNumber(self, n: int) -> int:
        result = []

        def generate_partitions(num_str, index=0, path=None, result=None):
            """ Generate all possible contiguous partitions of num_str """
            if path is None:
                path = []
            if result is None:
                result = []

            if index == len(num_str):  # If we reach the end, store the partition
                result.append(path[:])  
                return

            for end in range(index, len(num_str)):
                path.append(num_str[index:end+1])  # Take substring
                generate_partitions(num_str, end+1, path, result)  # Recur
                path.pop()  # Backtrack
            
            return result

        # Example Run

        def isValidSum(n):
            sq = n * n
            num_str = str(sq)
            partitions = generate_partitions(num_str)
            for partition in partitions:
                if sum(map(int, partition)) == n:
                    print(partition)
                    return True

            return False

        # Iterate through each element
        for num in range(1, n + 1):
            if isValidSum(num):
                result.append(num * num)

        # find its squares
        # check whether this sques val of sub string is equals to number
        # if anyone yes, then add to result

        return sum(result)
