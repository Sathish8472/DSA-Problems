/**
 * @param {number[][]} isWater
 * @return {number[][]}
 */

// BFS, Time: O(m * n), Space: O(m * n)
var highestPeak = function (isWater) {
    const m = isWater.length;
    const n = isWater[0].length;

    const height = Array.from({ length: m }, () => Array(n).fill(-1));
    const queue = [];

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (isWater[i][j] === 1) {
                height[i][j] = 0;
                queue.push([i, j]);
            }
        }
    }

    const directions = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ];

    let front = 0; // Efficient Deque-like traversal for TLE

    // Perform BFS
    while (front < queue.length) {
        const [x, y] = queue[front++]; //  This is expensive Opqueue.shift();
        for (const [dx, dy] of directions) {
            const nx = x + dx;
            const ny = y + dy;

            // Check if the neighbours are within the bounds and not visited
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && height[nx][ny] === -1) {
                height[nx][ny] = height[x][y] + 1;
                queue.push([nx, ny]);
            }
        }
    }

    return height;
};