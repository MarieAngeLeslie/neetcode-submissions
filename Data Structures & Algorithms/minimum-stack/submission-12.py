class MinStack:

    def __init__(self):
        self.customStack = []
        self.stackOfMinimum = []

    def push(self, val: int) -> None:
        self.customStack.append(val)
        new_value = min(val, self.stackOfMinimum[-1] if self.stackOfMinimum else val)
        self.stackOfMinimum.append(new_value)

    def pop(self) -> None:
        self.customStack.pop()
        self.stackOfMinimum.pop()
        
    def top(self) -> int:
        return self.customStack[-1]

    def getMin(self) -> int:
        return self.stackOfMinimum[-1]





