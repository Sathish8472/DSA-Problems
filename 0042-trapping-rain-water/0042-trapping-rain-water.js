/**
 * @param {number[]} height
 * @return {number}
 */

// Approach 2: Two pointers
// TC: O(n), SP: O(1)
var trap = function (height) {
    const n = height.length;

    if (n < 3) return 0;

    let left = 0, right = n - 1;
    let result = 0, maxLeft = 0, maxRight = 0;

    while (left <= right) {
        if (height[left] <= height[right]) {
            if (height[left] >= maxLeft) {
                maxLeft = height[left];
            } else {
                result += maxLeft - height[left];
            }
            left++;
        } else {
            if (height[right] >= maxRight) {
                maxRight = height[right];
            } else {
                result += maxRight - height[right];
            }
            right--;
        }
    }

    console.log(`Min: ${maxLeft}, right: ${maxRight}`);
    return result;
}



// Approach 1: Brute force
// TC: O(n ^ 2): The outer loop runs n − 2, and each inner loop runs up to \U0001d45b n times.
// SP: O(1)
var trap1 = function (height) {
    const n = height.length;

    if (n < 3) return 0;

    let result = 0;

    //Skipped calculations for the first and last bars since they cannot trap water.
    for (let i = 1; i < n - 1; i++) {
        let maxLeft = 0, maxRight = 0;

        // Calculate maxLeft for the current position
        for (let j = 0; j < i; j++) {
            maxLeft = Math.max(maxLeft, height[j]);
        }

        // Calculate maxRight for the current position
        for (let j = i; j < n; j++) {
            maxRight = Math.max(maxRight, height[j]);
        }

        // Calculate water trapped at the current position
        const water = Math.min(maxLeft, maxRight) - height[i];
        if (water > 0)
            result += water;
    }

    return result;
};