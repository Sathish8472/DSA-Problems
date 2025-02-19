/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {
    const rows = Array.from({ length: 9 }, () => new Set());
    const cols = Array.from({ length: 9 }, () => new Set());
    const boxes = Array.from({ length: 9 }, () => new Set());

    // Function to calculate the box index
    const getBoxIndex = (row, col) => Math.floor(row / 3) * 3 + Math.floor(col / 3);

    // Initialize the sets with existing board values
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            if (board[i][j] !== ".") {
                const num = board[i][j];
                rows[i].add(num);
                cols[j].add(num);
                boxes[getBoxIndex(i, j)].add(num);
            }
        }
    }

    const backtrack = (row, col) => {
        if (row === 9) return true; // Solved the entire board
        if (col === 9) return backtrack(row + 1, 0); // Move to the next row
        if (board[row][col] !== ".") return backtrack(row, col + 1); // Skip filled cells

        const boxIndex = getBoxIndex(row, col);

        for (let num = 1; num <= 9; num++) {
            const char = num.toString();

            if (!rows[row].has(char) && !cols[col].has(char) && !boxes[boxIndex].has(char)) {
                // Place the number
                board[row][col] = char;
                rows[row].add(char);
                cols[col].add(char);
                boxes[boxIndex].add(char);

                if (backtrack(row, col + 1)) return true;

                // Undo placement (backtrack)
                board[row][col] = ".";
                rows[row].delete(char);
                cols[col].delete(char);
                boxes[boxIndex].delete(char);
            }
        }

        return false; // No valid number can be placed
    };

    backtrack(0, 0);
};
