# @param {String} version1
# @param {String} version2
# @return {Integer}
def compare_version(version1, version2)
    version1 = version1.split(".").map(&:to_i)
    version2 = version2.split(".").map(&:to_i)
    i = j = 0
    while i < version1.length() and j < version2.length()
        if version1[i] < version2[j]
            return -1
        elsif version1[i] > version2[j]
            return 1
        end
        i += 1
        j += 1
    end
    if i < version1.length()
        while i < version1.length()
            if version1[i] != 0
                return 1
            end
            i += 1
        end
    elsif j < version2.length()
        while j < version2.length()
            if version2[j] != 0
                return -1
            end
            j += 1
        end
    end
    return 0
end