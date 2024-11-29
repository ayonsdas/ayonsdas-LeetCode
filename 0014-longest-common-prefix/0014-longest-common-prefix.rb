# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
    p = ""
    for i in 0..strs[0].length() - 1
        c = strs[0][i]
        strs.each do |st|
            if st.length() <= i or st[i] != c
                return p
            end
        end
        p += c
    end
    return p
end