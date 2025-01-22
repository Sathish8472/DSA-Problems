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

// DP
var highestPeak1 = function (isWater) {
    const m = isWater.length;
    const n = isWater[0].length;
    const INF = Infinity;

    // Initialize height matrix
    const height = Array.from({ length: m }, () => Array(n).fill(INF));
    
    // Set water cells to height 0
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (isWater[i][j] === 1) {
                height[i][j] = 0;
            }
        }
    }

    // Forward pass: top-left to bottom-right
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (height[i][j] !== 0) { // Skip water cells
                const top = i > 0 ? height[i - 1][j] : INF;
                const left = j > 0 ? height[i][j - 1] : INF;
                height[i][j] = Math.min(height[i][j], Math.min(top, left) + 1);
            }
        }
    }

    // Backward pass: bottom-right to top-left
    for (let i = m - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            if (height[i][j] !== 0) { // Skip water cells
                const bottom = i < m - 1 ? height[i + 1][j] : INF;
                const right = j < n - 1 ? height[i][j + 1] : INF;
                height[i][j] = Math.min(height[i][j], Math.min(bottom, right) + 1);
            }
        }
    }

    return height;
};