/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var i = 0;
    var j = 0;
    while(j < nums.length) {
        if(nums[i] != nums[j]) {
            nums[++i] = nums[j];
        }
        j++;
    }
    return i + 1;
};