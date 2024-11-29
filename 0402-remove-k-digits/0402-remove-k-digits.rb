# @param {String} num
# @param {Integer} k
# @return {String}
def remove_kdigits(num, k)
    s = Array.new([])
    num.split("").each do |n|
        while s.length() > 0 and k > 0 and s[-1].ord > n.ord
            s.pop()
            k -= 1
        end
        if s.length() > 0 or n != '0'
            s.push(n)
        end
    end
    if k
        if s.length() < k
            return '0'
        end
        s = s[0, s.length()-k]
    end
    s = s.join("")
    if s == ""
        return "0"
    end
    return s
end