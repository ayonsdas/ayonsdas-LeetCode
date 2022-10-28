class Solution:
    def trap(self, height):
        heightR = [0 for _ in range(len(height))]
        heightL = [0 for _ in range(len(height))]
        for i in range(1, len(height)):
            heightL[i] = max(heightL[i - 1], height[i - 1])
            heightR[~i] = max(heightR[-i], height[-i])
        x = 0
        for i in range(len(height)):
            x += max(0, min(heightL[i], heightR[i]) - height[i])
        return x