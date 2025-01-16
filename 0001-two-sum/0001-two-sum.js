/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

 // One-pass Hash table, TC: O(n), SP: O(n)
var twoSum = function (nums, target) {

    const map = new Map();
    for (var i = 0; i < nums.length; i++) {
        const k = target - nums[i];
        if (map.has(k)) {
            return [i, map.get(k)];
        } else {
            map.set(nums[i], i);
        }
    }

    console.log("No two sum solution found");
    return [];
};


// Two-pass Hash table, TC: O(n), SP: O(n)
var twoSum2 = function (nums, target) {
    const n = nums.length; 
    const map = new Map();

    for(let i = 0; i < n; i++){
        map.set(nums[i], i);
    }

    for(let i = 0; i < n; i++){
        const k = target - nums[i];

        // the checking element should not be current element
        if(map.has(k) && map.get(k) !== i){ 
            return [i, map.get(k)];
        }
    }

    return [];
} 

// Brute force, TC: O(n^2), SP: O(1)
var twoSum1 = function (nums, target) {
    const n = nums.length; 

    for(let i = 0; i < n; i++){
    
        for(let j = i + 1; j < n; j++){
    
            if(nums[j] === target - nums[i]){
                return [i, j];
            }
        }
    }

    return [];
}