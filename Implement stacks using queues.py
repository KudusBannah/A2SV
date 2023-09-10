class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        curr_len = len(self.queue)
        while curr_len:
            a = self.queue.popleft()
            self.queue.append(a)
            curr_len -= 1
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0