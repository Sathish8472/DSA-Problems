/**
 * @param {number[][]} isWater
 * @return {number[][]}
 */

 var highestPeak = function (isWater) {
    const m = isWater.length;
    const n = isWater[0].length;

    const height = Array.from({ length: m }, () => Array(n).fill(-1));
    const queue = [];
    
    // Initialize the queue with all water cells
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (isWater[i][j] === 1) {
                height[i][j] = 0;
                queue.push([i, j]); // Push water cells as the starting points
            }
        }
    }
    
    const directions = [
        [0, 1],  // East
        [1, 0],  // South
        [0, -1], // West
        [-1, 0]  // North
    ];
    
    let front = 0; // Efficient deque-like traversal

    // Perform BFS
    while (front < queue.length) {
        const [x, y] = queue[front++]; // Simulate deque using `front` index

        for (const [dx, dy] of directions) {
            const nx = x + dx;
            const ny = y + dy;

            // Check if the neighbor is within bounds and not visited
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && height[nx][ny] === -1) {
                height[nx][ny] = height[x][y] + 1;
                queue.push([nx, ny]); // Add new cell to the queue
            }
        }
    }
    
    return height;
};

var highestPeak1 = function (isWater) {
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

    //console.log("Q: ", queue);

    const directions = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ];

    // Perform BFS
    while (queue.length > 0) {
        const [x, y] = queue.shift();
        for (const [dx, dy] of directions) {
            const nx = x + dx;
            const ny = y + dy;

            // Check if the neighbours are within the bounds and not visited
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && height[nx][ny] === -1) {
                //console.log("inside");
                height[nx][ny] = height[x][y] + 1;
                queue.push([nx, ny]);
            }
        }
    }

    //console.log("H:", height);

    return height;
};