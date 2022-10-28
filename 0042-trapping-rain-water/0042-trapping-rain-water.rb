# @param {Integer[]} height
# @return {Integer}
def trap(height)
    heightL = [0]
    heightR = [0]
    for i in 1..height.length() - 1
        heightL.push([heightL[-1], height[i - 1]].max())
        heightR.unshift([heightR[0], height[-i]].max())
    end
    x = 0
    for i in 0..height.length() - 1
        x += [0, [heightL[i], heightR[i]].min() - height[i]].max()
    end
    return x
end 