/**
 * @param {number[]} nums
 * @param {number} limit
 * @return {number[]}
 */

var lexicographicallySmallestArray = function (nums, limit) {
    // Step 1: Sort the nums array and keep track of the original indices
    const numsSorted = [...nums];
    numsSorted.sort((a, b) => a - b);

    let currGroup = 0;
    const numToGroup = new Map(); // Map to store which group each element belongs to
    numToGroup.set(numsSorted[0], currGroup);

    const groupToList = new Map(); // Map to store lists of elements for each group
    groupToList.set(currGroup, [numsSorted[0]]);

    // Step 2: Create groups based on the limit
    for (let i = 1; i < numsSorted.length; i++) {
        if (Math.abs(numsSorted[i] - numsSorted[i - 1]) > limit) {
            // If difference exceeds limit, start a new group
            currGroup++;
        }
        numToGroup.set(numsSorted[i], currGroup);

        // Add the current number to the corresponding group list
        if (!groupToList.has(currGroup)) {
            groupToList.set(currGroup, []);
        }
        groupToList.get(currGroup).push(numsSorted[i]);
    }

    // Step 3: Reassign values to nums array based on the groups
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const group = numToGroup.get(num);
        // Pop the smallest element from the corresponding group
        nums[i] = groupToList.get(group).shift();
    }

    return nums;
}



// Brute, TC: O(n ^ 3), Outer while : N, For & for -> N ^ 2
var lexicographicallySmallestArray1 = function (nums, limit) {
    const n = nums.length;
    let swapped = true;

    while (swapped) {
        swapped = false;
        for (let i = 0; i < n - 1; i++) {
            for (let j = i + 1; j < n; j++) {

                if (Math.abs(nums[j] - nums[i]) <= limit && nums[j] < nums[i]) {
                    [nums[i], nums[j]] = [nums[j], nums[i]];
                    swapped = true;
                }
            }
        }
    }

    return nums;
};