/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */

 // Optimized
var xorAllNums = function(nums1, nums2) {
    let xorNums1 = 0;
    let xorNums2 = 0;

    for(const num of nums1){
        xorNums1 ^= num;
    }

    for(const num of nums2){
        xorNums2 ^= num;
    }

    const nums1CountOdd = nums1.length % 2 !== 0;
    const nums2CountOdd = nums2.length % 2 !== 0;

    const result = 
        (nums1CountOdd ? xorNums2 : 0) ^
        (nums2CountOdd ? xorNums1 : 0);

    return result;
};



 // Approach 2
var xorAllNums2 = function(nums1, nums2) {
    let result = 0;

    for(let i = 0; i < nums1.length; i++){
        for(let j = 0; j < nums2.length; j++){

            result ^= (nums1[i] ^ nums2[j]);
        }
    }

    return result;
};


// Approach 1

var xorAllNums1 = function(nums1, nums2) {
    const nums3 = [];

    for(let i = 0; i < nums1.length; i++){
        for(let j = 0; j < nums2.length; j++){

            nums2.push(nums1[i] ^ nums2[j]);
        }
    }


    let result = 0;
    for(const num of nums3){
        result ^= num;
    }

    return result;
};



