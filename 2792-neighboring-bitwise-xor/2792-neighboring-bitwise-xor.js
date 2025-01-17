/**
 * @param {number[]} derived
 * @return {boolean}
 */
var doesValidArrayExist = function (derived) {

    let xorDerived = 0;
    for(const num of derived){
        xorDerived ^= num;
    }

    return xorDerived === 0;
};