class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        min_abs_diff = min(arr[i+1]-arr[i] for i in range(n-1))
        return [[arr[i],arr[i+1]] for i in range(n-1) if arr[i+1]-arr[i] == min_abs_diff]
