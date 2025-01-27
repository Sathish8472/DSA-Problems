/**
 * @param {number[][]} grid
 * @return {number}
 */

// Tabulation
function minPathSum(grid) {
    const n = grid.length;
    const m = grid[0].length;

    const dp = new Array(n).fill(null).map(() => new Array(m).fill(0));

    // Loop through each cell in the matrix
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (i === 0 && j === 0) {
                // If we are at the top-left cell, set dp[i][j] to the value in the matrix
                dp[i][j] = grid[i][j];
            } else {
                // Calculate the sum of the current cell and the minimum of the two possible paths (from above and from the left)
                let up = grid[i][j];
                if (i > 0) up += dp[i - 1][j];
                else up += Infinity; // Set to a large value for the top row

                let left = grid[i][j];
                if (j > 0) left += dp[i][j - 1];
                else left += Infinity; // Set to a large value for the leftmost column

                // Store the minimum sum in dp[i][j]
                dp[i][j] = Math.min(up, left);
            }
        }
    }

    // The minimum sum path will be in dp[n-1][m-1]
    return dp[n - 1][m - 1];
}


// Memoization
var minPathSum1 = function (grid) {
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