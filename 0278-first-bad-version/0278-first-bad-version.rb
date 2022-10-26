# The is_bad_version API is already defined for you.
# @param {Integer} version
# @return {boolean} whether the version is bad
# def is_bad_version(version):

# @param {Integer} n
# @return {Integer}

def first_bad_version(n)
    l, r = 1, n
    while l < r
        m = (l + r) / 2
        if r - l >= 2
            if is_bad_version(m)
                r = m
            else
                l = m
            end
        else
            if is_bad_version(m)
                return m
            else
                return m + 1
            end
        end
    end
    return l
end 