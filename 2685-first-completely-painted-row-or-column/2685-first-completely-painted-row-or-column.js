/**
 * @param {number[]} arr
 * @param {number[][]} mat
 * @return {number}
 */


// Approach 2: Hash table

var firstCompleteIndex = function (arr, mat) {

    const m = mat.length;
    const n = mat[0].length;

    // Map values to their position in matrix
    const positionMap = new Map();
    for(let i = 0; i < m; i++){
        for(let j = 0; j < n; j++){
            positionMap.set(mat[i][j], [i, j]);
        }
    }

    // Track painted cells in row/cols
    const rowPaintCount = new Array(m).fill(0);
    const colPaintCount = new Array(n).fill(0);

    for(let i = 0 ; i < m * n; i++){
        const [row, col] = positionMap.get(arr[i]);

        // Paint the cell
        rowPaintCount[row]++;
        colPaintCount[col]++;

        // Check if any row/col is completely painted
        if(rowPaintCount[row] === n || colPaintCount[col] === m){
            return i;
        }
    }

    return -1;
}


 // Approach 1: Brute force
var firstCompleteIndex_1 = function (arr, mat) {
    const m = mat.length;
    const n = mat[0].length;

    const isAnyRowPainted = () => {
        for (let row = 0; row < m; row++) {
            if(mat[row].every(cell => cell === 0))
                return true;
        }

        return false;
    }

    const isAnyColPainted = () => {
        for (let col = 0; col < n; col++) {
            let isFullPainted = true;
            for(let row = 0; row < m; row++){
                if(mat[row][col] !== 0){
                    isFullPainted = false;
                    break;
                }
            }

            if (isFullPainted) return true;
        }

        return false;
    }

    for (let i = 0; i < arr.length; i++) {
        let paintValue = arr[i];

        for (let row = 0; row < m; row++) {
            for (let col = 0; col < n; col++) {
                if (mat[row][col] == paintValue) {
                    mat[row][col] = 0;
                }
            }
        }

        if (isAnyRowPainted(mat) || isAnyColPainted(mat)) {
            return i;
        }
    }

    return -1;
};