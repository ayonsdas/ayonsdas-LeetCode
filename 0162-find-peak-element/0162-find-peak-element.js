/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums)
{
    return search(nums, 0, nums.length - 1);
};

var search = function(nums, l, r)
{
    if (l == r)
        return l;
    var mid = l + Math.floor((r - l) / 2);
    if(nums[mid] > nums[mid + 1])
        return search(nums, l, mid);
    return search(nums, mid + 1, r);
}; 