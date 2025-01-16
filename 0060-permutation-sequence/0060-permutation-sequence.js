/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getPermutation = function(n, k) {
    let fact = 1;
    const numbers = [];
    
    for(let i = 1; i < n; i++){
        fact = fact * i;
        numbers.push(i);
    }

    numbers.push(n);

    let ans = "";
    k = k - 1;

    while(true){
        const index = Math.floor(k / fact);
        ans = ans + numbers[index];
        numbers.splice(index, 1); // Remove used number

        if(numbers.length === 0) break;

        k = k % fact;
        fact = Math.floor(fact / numbers.length);
    }

    return ans;
};