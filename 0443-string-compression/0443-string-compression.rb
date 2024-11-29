# @param {Character[]} chars
# @return {Integer}
def compress(chars)
    c = chars[0]
    i = 1
    j = 0
    t = 1
    while i < chars.length()
        if chars[i] == c
            t += 1
        else
            chars[j] = c
            j += 1
            if t != 1
                l = t.to_s
                for k in 0..l.length()-1
                    chars[j] = l[k]
                    j += 1
                end
            end
            t = 1
            c = chars[i]
        end
        i += 1
    end
    chars[j] = c
    j += 1
    if t != 1
        l = t.to_s
        for k in 0..l.length()-1
            chars[j] = l[k]
            j += 1
        end
    end
    return j
end