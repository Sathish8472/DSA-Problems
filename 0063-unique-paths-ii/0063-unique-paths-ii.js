/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function (obstacleGrid) {
    const m = obstacleGrid.length;
    const n = obstacleGrid[0].length;

    // If the start or end cell is blocked, no paths are possible
    if (obstacleGrid[0][0] === 1 || obstacleGrid[m - 1][n - 1] === 1) {
        return 0;
    }

    let prev = new Array(n).fill(0);
    prev[0] = 1; // Start position

    for (let i = 0; i < m; i++) {
        let temp = new Array(n).fill(0);

        for (let j = 0; j < n; j++) {
            if (obstacleGrid[i][j] === 1) {
                temp[j] = 0; // No path through obstacles
            } else {
                if (i === 0 && j === 0) {
                    temp[j] = 1; // Start position
                } else {
                    let up = i > 0 ? prev[j] : 0;
                    let left = j > 0 ? temp[j - 1] : 0;
                    temp[j] = up + left;
                }
            }
        }

        prev = temp; // Update for the next row
    }

    return prev[n - 1];
};

