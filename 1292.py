class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        prefixSum = [[0]*(n+1) for _ in range(m+1)]
        for y in range(1,m+1):
            for x in range(1,n+1):
                prefixSum[y][x] = mat[y-1][x-1] + prefixSum[y-1][x] + prefixSum[y][x-1] - prefixSum[y-1][x-1]
        for k in reversed(range(min(m,n))):
            for y in range(1,m-k+1):
                for x in range(1,n-k+1):
                    if prefixSum[y+k][x+k] - prefixSum[y-1][x+k] - prefixSum[y+k][x-1] + prefixSum[y-1][x-1] <= threshold:
                        return k + 1
        return 0
