class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        self.queue = deque()
        self.curr = False
        

    def consec(self, num: int) -> bool:
        self.queue.appendleft(num)
        if len(self.queue) < self.k:
            return False
        
        if self.k > 1 and self.queue[0] == self.queue[1] and self.curr:
            return True

        for i in range(self.k):
            if self.queue[i] != self.value:
                self.curr = False
                return False
        self.curr = True
        return True
        