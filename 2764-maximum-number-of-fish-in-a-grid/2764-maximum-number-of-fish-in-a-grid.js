/**
 * @param {number[][]} grid
 * @return {number}
 */

// DFS & BFS, TC: O(M x N), SP: O(M x N)
var findMaxFish = function (grid) {
    const m = grid.length;
    const n = grid[0].length;
    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    let result = 0;

    const visited = Array.from({ length: m }, () => Array(n).fill(false));
    //console.log(visited);

    const isValid = (x, y) => x >= 0 && y >= 0 && x < m && y < n && grid[x][y] > 0 && !visited[x][y];

    // DFS implementation
    const dfs = (x, y) => {
        visited[x][y] = true;
        let fish = grid[x][y];

        for (const [dx, dy] of directions) {
            const nx = x + dx;
            const ny = y + dy;

            if (isValid(nx, ny)) {
                fish += dfs(nx, ny);
                console.log(fish);
            }
        }

        return fish;
    };

    // BFS implementation
    const bfs = (x, y) => {
        const queue = [[x, y]];
        visited[x][y] = true;
        let fish = 0;

        while (queue.length > 0) {
            const [cx, cy] = queue.shift();
            fish += grid[cx][cy];

            for (const [dx, dy] of directions) {
                const nx = cx + dx, ny = cy + dy;
                if (isValid(nx, ny)) {
                    visited[nx][ny] = true;
                    queue.push([nx, ny]);
                }
            }
        }
        console.log(fish);
        return fish;
    };

    let maxFish = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] > 0 && !visited[i][j]) {
                maxFish = Math.max(maxFish, bfs(i, j));
            }
        }
    }

    //console.log(visited);

    return maxFish;
};