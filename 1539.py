class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        return sorted(set(range(1, 2002)) ^ set(arr))[k - 1]
