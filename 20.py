class Solution:
    def isValid(self, s: str) -> bool:
        front = "({["
        back = ")}]"
        brackets = []
        for b in s:
            if b in back and brackets and brackets[-1] == front[back.index(b)]:
                brackets.pop()
            else:
                brackets.append(b)
        return len(brackets) == 0
