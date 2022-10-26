# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
    i = j = 0
    while j < nums.length()
        if nums[i] != nums[j]
            i += 1
            nums[i] = nums[j]
        end
        j += 1
    end
    return i + 1
end