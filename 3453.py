from heapq import heapify, heappop

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        down, up, slope = 0, 0, 0
        heap = []
        for square in squares:
            _, y, l = square
            heap.append((y, l, 0))
            heap.append((y+l, l, 1))
            up += int(l**2)
        heapify(heap)
        prevY = 0
        while heap:
            y, l, end = heappop(heap)
            if slope != 0:
                sol = (up - down)/(2 * slope)
                if sol + prevY <= y:
                    return sol + prevY
            down += slope * (y - prevY)
            up -= slope * (y - prevY)
            if not end:
                slope += l
            else:
                slope -= l
            prevY = y
