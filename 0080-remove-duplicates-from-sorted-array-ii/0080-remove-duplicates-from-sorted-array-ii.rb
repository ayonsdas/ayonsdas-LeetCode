# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
    c = 1
    curr = 10001
    i = 0
    j = 0
    while j < nums.length()
        if nums[j] != curr
            curr = nums[j]
            c = 0
        end
        c = c + 1
        if c < 3
            nums[i] = nums[j]
            i = i + 1
        end
        j = j + 1
    end
    return i
end