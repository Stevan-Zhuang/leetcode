class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if not n in counts:
                counts[n] = 0
            counts[n] += 1
        counts_array = [(k, counts[k]) for k in counts]
        counts_array.sort(key=lambda x: x[1], reverse=True)
        return [counts_array[n][0] for n in range(k)]
