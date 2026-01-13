
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        i = 0
        j = n - 1
        while i != j:
            sol = min(height[i], height[j]) * (j - i)
            res = max(res, sol)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return res
