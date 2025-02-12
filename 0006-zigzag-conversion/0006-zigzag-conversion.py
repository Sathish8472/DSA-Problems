class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        matrix = [[""] * len(s) for _ in range(numRows)]
        row, col = 0, 0
        going_down = True

        for char in s:
            matrix[row][col] = char  # Place the character in the matrix
            if going_down:
                if row == numRows - 1:  # Reached the bottom row
                    going_down = False
                    row -= 1
                    col += 1
                else:
                    row += 1
            else:
                if row == 0:  # Reached the top row
                    going_down = True
                    row += 1
                else:
                    row -= 1
                    col += 1

        # Read the matrix row by row
        result = []
        for r in matrix:
            for c in r:
                if c:  # Ignore empty cells
                    result.append(c)

        return "".join(result)
