class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        while idx < len(nums) - 2:
            if nums[idx] == nums[idx + 1] == nums[idx + 2]:
                nums.pop(idx)
                idx -= 1
            idx += 1
        return idx + 2
        
