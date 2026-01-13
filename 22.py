class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = []
        q.append(["", 0, n])
        res = []
        while q:
            brackets, open_b, nx = q.pop()
            if nx == 0:
                res.append(brackets)
                continue
            if open_b:
                q.append([brackets + ")", open_b - 1, nx - 1])
            if open_b < nx:
                q.append([brackets + "(", open_b + 1, nx])
        return res
