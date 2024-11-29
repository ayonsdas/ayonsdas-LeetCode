/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var hammingWeight = function(n) {
    var c = 0;
    while(n != 0)
    {
        if(n & 1 != 0)
        {
             c += 1;
        }
        n >>>= 1;
    }
    return c;
};