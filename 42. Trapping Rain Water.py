class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        upp, res = 0, 0
        while l < r:
            low  = min(height[l], height[r])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            upp = max(upp, low)
            res += (upp- low)
        return res
