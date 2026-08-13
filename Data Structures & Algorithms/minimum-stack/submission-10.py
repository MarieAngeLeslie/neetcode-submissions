class MinStack:

    def __init__(self):
        self.customStack = []
        self.stackOfMinimum = []

    def push(self, val: int) -> None:
        if self.stackOfMinimum : 
            if val < self.stackOfMinimum[-1] : 
                self.stackOfMinimum.append(val)
            else : 
                self.stackOfMinimum.append(self.stackOfMinimum[-1])
        else : 
             self.stackOfMinimum.append(val)   

        self.customStack.append(val)

    def pop(self) -> None:
        self.customStack.pop()
        self.stackOfMinimum.pop()
        
    def top(self) -> int:
        return self.customStack[-1]

    def getMin(self) -> int:
        return self.stackOfMinimum[-1]





