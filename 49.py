class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for s in strs:
            ana = ''.join(sorted(s))
            if not ana in grouped:
                grouped[ana] = []
            grouped[ana].append(s)
        return [grouped[s] for s in grouped]
