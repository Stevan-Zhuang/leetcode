from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        dist = [float('inf')]*n
        dist[0] = 0
        g = defaultdict(list)
        gs = defaultdict(list)
        for (u,v,w) in edges:
            g[u].append((v,w))
            gs[v].append((u,w))
        q = [(0,0)]
        while q:
            c, u = heappop(q)
            if u == n - 1:
                return int(dist[u])
            if c > dist[u]:
                continue
            for (v, w) in g[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heappush(q, (dist[u] + w, v))
            for (v, w) in gs[u]:
                w *= 2
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heappush(q, (dist[u] + w, v))
        return -1
