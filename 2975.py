class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]
        h_lengths = set()
        h = len(hFences)
        v = len(vFences)
        for i in range(h):
            for j in range(i + 1, h):
                h_lengths.add(abs(hFences[j] - hFences[i]))
        max_len = -1
        for i in range(v):
            for j in range(i + 1, v):
                v_len = abs(vFences[j] - vFences[i])
                if v_len in h_lengths:
                    max_len = max(max_len, v_len)

        return (max_len**2) % (10**9 + 7) if max_len > 0 else -1
