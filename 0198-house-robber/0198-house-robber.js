/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    const n = nums.length;
    let prev = nums[0];
    let prev2 = 0;

    for(let i = 1; i < n; i++){
        let pick = nums[i];

        if(i > 1)
            pick += prev2;

        let notPick = 0 + prev;

        let cur_i = Math.max(pick, notPick);
        prev2 = prev;
        prev = cur_i;
    }

    return prev;
};