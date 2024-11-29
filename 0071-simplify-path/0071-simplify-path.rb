# @param {String} path
# @return {String}
def simplify_path(path)
    path = path.split("/")
    s = []
    for i in 0..path.length()-1
        if path[i] == ".."
            if s
                s.pop()
            end
        elsif path[i] == "." or path[i] == ""
            next
        else
            s << path[i]
        end
    end
    return "/" + s.join("/")
end