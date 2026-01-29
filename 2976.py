from heapq import heappush, heappop
from collections import defaultdict
from math import isinf
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        letters = set(list(source) + list(target) + original + changed)
        dist = {l1: {l2: float('inf') for l2 in letters} for l1 in letters}
        for u, v, w in zip(original, changed, cost):
            graph[u].append((v,w))

        total = 0
        for x, y in zip(source, target):
            if x == y:
                continue
            if not isinf(dist[x][y]):
                total += dist[x][y]
                continue

            dist[x][x] = 0
            q = [(0, x)]
            while q:
                c, u = heappop(q)
                if c > dist[x][u]:
                    continue
                for (v, w) in graph[u]:
                    nc = c + w
                    if nc < dist[x][v]:
                        dist[x][v] = nc
                        heappush(q, (nc, v))
            if isinf(dist[x][y]):
                return -1
            total += dist[x][y]

        return total
