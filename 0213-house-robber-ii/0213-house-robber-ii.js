/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {

    const solve = (arr) => {
        const n = arr.length;
        let prev = arr[0];
        let prev2 = 0;

        for (let i = 1; i < n; i++) {
            let pick = arr[i];

            if (i > 1)
                pick += prev2;

            let notPick = 0 + prev;

            let cur_i = Math.max(pick, notPick);
            prev2 = prev;
            prev = cur_i;
        }

        return prev;
    };

    const n = nums.length;
    let temp1 = [];
    let temp2 = [];

    if(n === 1) return nums[0];

    for (let i = 0; i < nums.length; i++) {
        if (i != n - 1)
            temp1.push(nums[i]);

        if (i !== 0)
            temp2.push(nums[i]);
    }

    return Math.max(solve(temp1), solve(temp2));
};