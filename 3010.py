class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        nums.pop(0)
        return first + sum(sorted(nums)[:2])
