/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function (nums) {
    const n = nums.length;
    let arr = nums;


    let totSum = 0;

    // Calculate the total sum of elements in the array
    for (let i = 0; i < n; i++) {
        totSum += arr[i];
    }

    // If the total sum is odd, it cannot be partitioned into two equal subsets
    if (totSum % 2 === 1) return false;
    else {
        const k = totSum / 2;

        // Initialize the previous row (array) for dynamic programming
        let prev = new Array(k + 1).fill(false);
        prev[0] = true;

        // Initialize the first column of the dp array
        if (arr[0] <= k) {
            prev[arr[0]] = true;
        }

        // Fill the dp array using bottom-up dynamic programming
        for (let ind = 1; ind < n; ind++) {
            const cur = new Array(k + 1).fill(false);
            cur[0] = true;
            for (let target = 1; target <= k; target++) {
                const notTaken = prev[target];

                let taken = false;
                if (arr[ind] <= target) {
                    taken = prev[target - arr[ind]];
                }

                cur[target] = notTaken || taken;
            }
            // Update the previous row (array) for the next iteration
            prev = cur;
        }

        // The final element of the 'prev' array (prev[k]) contains the result
        return prev[k];
    }
}
