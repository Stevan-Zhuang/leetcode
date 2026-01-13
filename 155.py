class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min = val
            return

        if val < self.min:
            self.stack.append(2 * val - self.min)
            self.min = val
        else:
            self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val < self.min:
            self.min = 2 * self.min - val

    def top(self) -> int:
        val = self.stack[-1]
        if val < self.min:
            return self.min
        return val

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
