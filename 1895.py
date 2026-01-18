def is_magic_square(prefixH, prefixV, prefixDL, prefixDR, k, y, x):
    magic_sum = prefixDL[y+k-1][x+k-1] - prefixDL[y-1][x-1]
    if prefixDR[y+k-1][x] - prefixDR[y-1][x+k] != magic_sum:
        return False
    for kk in range(k):
        if prefixH[y+kk][x+k-1] - prefixH[y+kk][x-1] != magic_sum:
            return False
        if prefixV[y+k-1][x+kk] - prefixV[y-1][x+kk] != magic_sum:
            return False
    return True

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        prefixH = [[0]*(m+1) for _ in range(n+1)]
        prefixV = [[0]*(m+1) for _ in range(n+1)]
        prefixDL = [[0]*(m+2) for _ in range(n+2)]
        prefixDR = [[0]*(m+2) for _ in range(n+2)]

        for y in range(1,n+1):
            for x in range(1,m+1):
                prefixH[y][x] = grid[y-1][x-1] + prefixH[y][x-1]
                prefixV[y][x] = grid[y-1][x-1] + prefixV[y-1][x]
                prefixDL[y][x] = grid[y-1][x-1] + prefixDL[y-1][x-1]
                prefixDR[y][x] = grid[y-1][x-1] + prefixDR[y-1][x+1]

        for k in reversed(range(2,min(n,m)+1)):
            for y in range(1,n-k+2):
                for x in range(1,m-k+2):
                    if is_magic_square(prefixH, prefixV, prefixDL, prefixDR, k, y, x):
                        return k
        return 1
