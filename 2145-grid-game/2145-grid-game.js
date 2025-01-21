/**
 * @param {number[][]} grid
 * @return {number}
 */
var gridGame = function(grid) {
    const n = grid[0].length;

    const prefixTop = Array(n).fill(0);
    const prefixBottom = Array(n).fill(0);

    prefixTop[0] = grid[0][0];
    prefixBottom[0] = grid[1][0];
    
    for(let i = 1; i < n; i++){
        prefixTop[i] = prefixTop[i - 1] + grid[0][i];
        prefixBottom[i] = prefixBottom[i - 1] + grid[1][i];
    }

    let result = Infinity;
    for(let i = 0; i < n; i++){
        const top = i < n - 1 ? prefixTop[n - 1] - prefixTop[i] : 0;
        const bottom = i > 0 ? prefixBottom[i - 1] : 0;

        const secondRobotScore = Math.max(top, bottom); // Robots 2's Max score
        result = Math.min(result, secondRobotScore);    // Minimize the Max score
    }

    return result;
};