class Solution:

    # Greedy stack Approach
    # Time: O(N), Space: O(N)
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result = ""
        stack = []

        for i in range(n + 1):
            stack.append(i + 1)

            if i == n or pattern[i] == "I":
                while stack:
                    result += str(stack.pop())

        return result


        

    # Backtracking - NOT Optimal
    # Time: O(N!), Space: O(N) recursive depth stack space
    def smallestNumber_1(self, pattern: str) -> str:
        result = []
        used = [False] * 10  # Space: O(10)
        print(used)

        def backtrack(curr_str):
            if len(curr_str) == len(pattern) + 1:
                result.append(curr_str)
                return

            for digit in range(1, 10):
                if used[digit]:
                    continue

                if curr_str:
                    last_digit = int(curr_str[-1])
                    if pattern[len(curr_str) - 1] == "I" and last_digit > digit:
                        continue
                    if pattern[len(curr_str) - 1] == "D" and last_digit < digit:
                        continue

                used[digit] = True  # time: O(1)
                backtrack(curr_str + str(digit))  # Recursive call: O(N!)
                used[digit] = False  # time: O(1)

                if result:
                    return

        backtrack("")
        return result[0]
