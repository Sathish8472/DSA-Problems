/**
 * @param {number[][]} grid
 * @return {number}
 */

// Memoization
var minPathSum = function (grid) {
    // Get the dimensions of the matrix
    const n = grid.length;
    const m = grid[0].length;

    // Create a 2D array 'dp' to store intermediate results (memoization)
    const dp = new Array(n).fill(null).map(() => new Array(m).fill(-1));

    // Define a recursive utility function to find the minimum sum path
    function minSumPathUtil(i, j) {
        if (i === 0 && j === 0) {
            return grid[0][0];
        }
        if (i < 0 || j < 0) {
            return Infinity;
        }

        // If the result for this cell has already been calculated, return it
        if (dp[i][j] !== -1) {
            return dp[i][j];
        }

        // Calculate the sum of the current cell and the minimum of the two possible paths
        const up = grid[i][j] + minSumPathUtil(i - 1, j);
        const left = grid[i][j] + minSumPathUtil(i, j - 1);

        // Store the result for this cell in the memoization table and return it
        dp[i][j] = Math.min(up, left);
        return dp[i][j];
    }

    // Start the recursive calculation from the bottom-right cell
    return minSumPathUtil(n - 1, m - 1);
}