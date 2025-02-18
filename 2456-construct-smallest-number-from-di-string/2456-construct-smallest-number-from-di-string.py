class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        used = [False] * 10

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

                used[digit] = True
                backtrack(curr_str + str(digit))
                used[digit] = False
                if result:
                    return

        backtrack("")
        return result[0]
