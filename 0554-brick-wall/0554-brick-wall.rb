# @param {Integer[][]} wall
# @return {Integer}
def least_bricks(wall)
    stuff = Hash.new()
    for i in 0..wall.length()-1
        k = 0
        for j in 0..wall[i].length()-2
            k += wall[i][j]
            if not stuff.key?(k)
                stuff[k] = 0
            end
            stuff[k] = stuff[k] + 1
        end
    end
    if stuff.empty?()
        return wall.length()
    end
    return wall.length() - stuff[stuff.max_by{|k, v| v}[0]]
end 