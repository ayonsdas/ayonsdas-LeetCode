# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
    c = 1
    curr = 10001
    i = 0
    j = 0
    for j in 0..nums.length() - 1
        if nums[j] != curr
            curr = nums[j]
            c = 0
        end
        c += 1
        if c < 3
            nums[i] = nums[j]
            i += 1
        end
    end
    return i
end 