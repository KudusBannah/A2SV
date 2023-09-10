class MyQueue:

    def __init__(self):
        self.stack = deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        curr_len = len(self.stack)
        while curr_len-1:
            a = self.stack.pop()
            self.stack.appendleft(a)
            curr_len -= 1
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return len(self.stack) == 0