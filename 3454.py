from typing import List
from heapq import heapify, heappop

class SegmentTreeNode:
    def __init__(self, span):
        self.left = None
        self.right = None
        self.count = 0
        self.span = span
        self.length = 0

def update(node, node_l, node_r, a, b, delta):
    if node_r <= a or node_l >= b: 
        return
    if a <= node_l and node_r <= b: 
        node.count += delta
    else:
        mid = (node_l + node_r)//2
        if node.left is None:
            node.left = SegmentTreeNode(mid - node_l)
        if node.right is None:
            node.right = SegmentTreeNode(node_r - mid)
        update(node.left, node_l, mid, a, b, delta)
        update(node.right, mid, node_r, a, b, delta)

    if node.count > 0:
        node.length = node_r - node_l
    else:
        if node.left is None:
            node.length = 0
        else:
            node.length = node.left.length + node.right.length

def get_total_area(squares):
    area, slope = 0, 0
    heap = []
    for square in squares:
        x, y, l = square
        heap.append((y, x, l, 1))
        heap.append((y+l, x, l, -1))
    heapify(heap)

    root_start = 0
    root_end = int(2*10**9)
    line_union_segment_tree = SegmentTreeNode(root_end - root_start)

    prevY = 0
    while heap:
        y = heap[0][0]
        if y - prevY > 0:
            area += slope * (y - prevY)
        while heap and heap[0][0] == y:
            _, x, l, end = heappop(heap)
            update(line_union_segment_tree, root_start, root_end, x, x + l, end)

        slope = line_union_segment_tree.length
        prevY = y
    return area

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        down, up, slope = 0, get_total_area(squares), 0
        heap = []
        for square in squares:
            x, y, l = square
            heap.append((y, x, l, 1))
            heap.append((y+l, x, l, -1))
        heapify(heap)

        root_start = 0
        root_end = int(2*10**9)
        line_union_segment_tree = SegmentTreeNode(root_end - root_start)

        prevY = 0
        while heap:
            y = heap[0][0]
            dy = y - prevY

            if slope > 0:
                sol = (up - down) / (2 * slope)
                if sol <= dy:
                    return prevY + sol

            down += slope * dy
            up -= slope * dy

            while heap and heap[0][0] == y:
                _, x, l, end = heappop(heap)
                update(line_union_segment_tree, root_start, root_end, x, x + l, end)

            slope = line_union_segment_tree.length
            prevY = y

        return 0.0
