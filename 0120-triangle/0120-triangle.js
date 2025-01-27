/**
 * @param {number[][]} triangle
 * @return {number}
 */

// Tabulation, TC: O(N * N), SP: O(N * N)
var minimumTotal = function (triangle) {
    const n = triangle.length;

    let front = new Array(n).fill(0);
    let cur = new Array(n).fill(0);

    for (let j = 0; j < n; j++) {
        front[j] = triangle[n - 1][j];
    }

    for (let i = n - 2; i >= 0; i--) {
        for (let j = 0; j <= i; j++) {
            const down = triangle[i][j] + front[j];
            const diagonal = triangle[i][j] + front[j + 1];

            cur[j] = Math.min(down, diagonal);
        }

        front = [...cur];
    }

    return front[0];
};


// Memoization, TC: O(N * N), SP: O(N * N)
var minimumTotal1 = function (triangle) {
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