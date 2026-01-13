class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        max_stack = [(temperatures[n - 1], n - 1)]
        res = [0] * n
        for i in reversed(range(n - 1)):
            t = temperatures[i]

            while max_stack and t >= max_stack[-1][0]:
                max_stack.pop()
            if max_stack and t < max_stack[-1][0]:
                res[i] = max_stack[-1][1] - i

            max_stack.append((t, i))
        return res
