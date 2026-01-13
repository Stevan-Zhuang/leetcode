class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        t_map = {}
        for i, n in enumerate(numbers):
            if n in t_map:
                i_2 = t_map[n]
                return [i_2 + 1, i + 1]
            t_map[target - n] = i

