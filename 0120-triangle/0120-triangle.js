/**
 * @param {number[][]} triangle
 * @return {number}
 */

// Memoization
var minimumTotal = function (triangle) {
    const n = triangle.length;

    const dp = new Array(n).fill().map(() => new Array(n).fill(-1));

    const minimumPathSumUtil = (i, j) => {
        if (dp[i][j] != -1)
            return dp[i][j];

        if (i === n - 1) return triangle[i][j];

        const down = triangle[i][j] + minimumPathSumUtil(i + 1, j);
        const diagonal = triangle[i][j] + minimumPathSumUtil(i + 1, j + 1);

        dp[i][j] = Math.min(down, diagonal);
        return dp[i][j];
    }

    return minimumPathSumUtil(0, 0);
};