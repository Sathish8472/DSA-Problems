class Solution:

    def punishmentNumber(self, n: int) -> int:

        def generate_partitions(num_str, index=0, path=None, result=None):
            """Generate all possible contiguous partitions of num_str"""
            if path is None:
                path = []
            if result is None:
                result = []

            if index == len(num_str):  # If we reach the end, store the partition
                result.append(path[:])
                return

            for end in range(index, len(num_str)):
                path.append(num_str[index : end + 1])  # Take substring
                generate_partitions(num_str, end + 1, path, result)  # Recur
                path.pop()  # Backtrack

            return result

        def can_partition_to_target(num_str, target):
            partitions = generate_partitions(num_str)
            for partition in partitions:
                if sum(map(int, partition)) == target:
                    return True
            return False

        punishment_sum = 0

        for i in range(1, n + 1):
            print(i)
            square_str = str(i * i)
            if can_partition_to_target(square_str, i):
                punishment_sum += i * i
                

        return punishment_sum
