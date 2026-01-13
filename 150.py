class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda x, y: int(x) + int(y),
            "-": lambda x, y: int(x) - int(y),
            "*": lambda x, y: int(x) * int(y),
            "/": lambda x, y: int(x) / int(y),
        }
        for t in tokens:
            if t in ops:
                x = stack.pop()
                y = stack.pop()
                stack.append(ops[t](y, x))
            else:
                stack.append(t)
        return int(stack[0])
