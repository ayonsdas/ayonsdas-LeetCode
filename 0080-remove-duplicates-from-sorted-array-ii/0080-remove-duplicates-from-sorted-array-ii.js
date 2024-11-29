/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var c = 1;
    var curr = 10001;
    var i = 0;
    for(let j = 0; j < nums.length; j++) {
        if(nums[j] != curr) {
            curr = nums[j];
            c = 0;
        }
        c += 1;
        if(c < 3) {
            nums[i++] = nums[j];
        }
    }
    return i;
};