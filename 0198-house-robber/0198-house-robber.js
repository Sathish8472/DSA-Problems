/**
 * @param {number[]} nums
 * @return {number}
 */
var rob1 = function (nums) {
    const n = nums.length;
    let prev = nums[0];
    let prev2 = 0;

    for (let i = 1; i < n; i++) {
        let pick = nums[i];

        if (i > 1)
            pick += prev2;

        let notPick = 0 + prev;

        let cur_i = Math.max(pick, notPick);
        prev2 = prev;
        prev = cur_i;
    }

    return prev;
};

var rob = function (nums) {

    const solve = (ind, nums, dp) => {

        if (ind === 0) return nums[ind];
        if (ind < 0) return 0;

        if (dp[ind] !== -1)
            return dp[ind];

        let pick = nums[ind] + solve(ind - 2, nums, dp);
        let notPick = 0 + solve(ind - 1, nums, dp);

        dp[ind] = Math.max(pick, notPick);
        return dp[ind];
    };

    const n = nums.length;
    let dp = new Array(n).fill(-1);
    return solve(n - 1, nums, dp);

};