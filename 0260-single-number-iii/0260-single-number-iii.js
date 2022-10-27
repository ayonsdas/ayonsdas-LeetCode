/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
    var x = 0;
    for(let i = 0; i < nums.length; i++)
        x ^= nums[i];
    var aX = x, p = 0;
    while(true)
    {
        if(aX % 2 != 0)
            break;
        p += 1;
        aX /= 2;
    }
    var n1 = 0, n2 = 0;
    for(var j = 0; j < nums.length; j++)
    {
        if((nums[j] & Math.pow(2, p)) == 0)
            n1 = n1 ^ nums[j];
        else
            n2 = n2 ^ nums[j];
    }
    return [n1, n2];
};