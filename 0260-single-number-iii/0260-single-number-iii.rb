# @param {Integer[]} nums
# @return {Integer[]}
def single_number(nums)
    x = 0
    nums.each do |num|
        x ^= num
    end
    aX = x
    p = 0
    while true
        if aX % 2 != 0
            break
        end
        p += 1
        aX /= 2
    end
    n1, n2 = 0, 0
    nums.each do |num|
        if num & 2 ** p == 0
            n1 ^= num
        else
            n2 ^= num
        end
    end
    return Array.new([n1, n2])
end