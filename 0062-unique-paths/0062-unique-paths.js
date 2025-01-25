/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function (m, n) {
    let N = m + n - 2;
    let r = m - 1;
    let result = 1;

    for (let i = 1; i <= r; i++) {
        result = result * (N - r + i) / i;
    }

    return result;
};