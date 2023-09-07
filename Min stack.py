class MinStack:
    
    def __init__(self):
        self.stack = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(val)
        elif val <= self.mins[-1]:
            self.mins.append(val)
        

    def pop(self) -> None:
        popped = self.stack.pop() 
        if self.mins[-1] == popped:
            self.mins.pop()
        return popped
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]