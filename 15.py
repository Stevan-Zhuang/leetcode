class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count_map = {}
        for num in nums:
            if not num in count_map:
                count_map[num] = 0
            count_map[num] += 1

        n = len(nums)
        res = set()
        for i in range(n):
            for j in range(i + 1, n):
                x, y = nums[i], nums[j]
                target = -(x + y)
                if target in count_map:
                    avail = count_map[target]
                    for z in [x, y]:
                        if z == target:
                            avail -= 1
                    if avail > 0:
                        res.add(tuple(sorted([x, y, target])))
        return map(list, res)
