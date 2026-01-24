class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        min_max = 0 
        for i in range(n//2):
            min_max = max(min_max, nums[i] + nums[n-1-i])
        return min_max
