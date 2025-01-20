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
var firstCompleteIndex1 = function (arr, mat) {
    const len = arr.length;
    const m = mat.length;
    const n = mat[0].length;
    let index = 0;

    const isAnyRowPainted = (mat) => {
        
        for (let x = 0; x < m; x++) {
            let count = 0;
            for (let y = 0; y < n; y++) {
                if (mat[x][y] === 0) {
                    count++;
                }
            }

            if (count === n) {
                return true;
            }
        }
        
        console.log(`Mat in row: ${mat} `);
        return false;
    }

    function isAnyColPainted(mat) {
        for (let x = 0; x < n; x++) {
            let count = 0;
            for (let y = 0; y < m; y++) {
                if (mat[y][x] === 0) {
                    count++;
                }
            }

            if (count === m) {
                return true;
            }
        }

        return false;
    }

    for (let i = 0; i < len; i++) {
        let paintValue = arr[i];

        for (let j = 0; j < m; j++) {
            for (let k = 0; k < n; k++) {
                if (mat[j][k] == paintValue) {
                    mat[j][k] = 0;
                }
            }
        }

        if (isAnyRowPainted(mat) || isAnyColPainted(mat)) {
            index = i;
            break;
        }
    }

    return index;
};