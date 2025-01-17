/**
 * @param {number[]} derived
 * @return {boolean}
 */
var doesValidArrayExist = function (derived) {

    let xorSum = 0;
    for(const num of derived){
        xorSum ^= num;
    }

     // If the XOR sum is 0, a valid original array exists
    return xorSum === 0;
};