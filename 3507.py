def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        while not is_sorted(nums):
            min_sum_pair = nums[0] + nums[1]
            idx = 0
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < min_sum_pair:
                    min_sum_pair = nums[i] + nums[i + 1]
                    idx = i
            for _ in range(2):
                nums.pop(idx)
            nums.insert(idx, min_sum_pair)
            count += 1
        return count
