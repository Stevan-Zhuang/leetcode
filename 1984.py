class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = (10**5)+1
        for i in range(len(nums) - k + 1):
            min_diff = min(min_diff, nums[i+k-1] - nums[i])
        return min_diff
