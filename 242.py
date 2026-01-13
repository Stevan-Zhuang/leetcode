class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        all_l = set()
        for l in s:
            if l not in s_count:
                s_count[l] = 0
            s_count[l] += 1
            all_l.add(l)
        for l in t:
            if l not in t_count:
                t_count[l] = 0
            t_count[l] += 1
            all_l.add(l)
        for l in all_l:
            if not l in s_count:
                return False
            if not l in t_count:
                return False
            if s_count[l] != t_count[l]:
                return False
        return True
