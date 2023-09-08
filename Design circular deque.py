class NodeList:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.MAX = k
        self.length = 0
        self.rear = self.front = None

    def insertFront(self, value: int) -> bool:
        if self.length == self.MAX:
            return False
        new_node = NodeList(value)
        if self.length == 0:
            self.rear = self.front = new_node
        else:
            self.front.next = new_node
            new_node.prev = self.front
            self.front = new_node
        self.length += 1
        return True
        
        
    def insertLast(self, value: int) -> bool:
        if self.length == self.MAX:
            return False
        new_node = NodeList(value)
        if self.length == 0:
            self.rear = self.front = new_node
        else:
            self.rear.prev = new_node
            new_node.next = self.rear
            self.rear = new_node
        self.length += 1
        return True 
        

    def deleteFront(self) -> bool:
        if not self.length:
            return False
        prev = self.front.prev
        self.front.prev = None
        self.front = prev
        if prev:
            prev.next = None
        self.length -= 1
        return True
        

    def deleteLast(self) -> bool:
        if not self.length:
            return False
        next_ = self.rear.next
        self.rear.next = None
        self.rear = next_
        if next_:
            next_.prev = None
        self.length -= 1
        return True

        
    def getFront(self) -> int:
        if self.length:
            return self.front.val
        return -1
        

    def getRear(self) -> int:
        if self.length:
            return self.rear.val
        return -1
        

    def isEmpty(self) -> bool:
        return self.length == 0
        

    def isFull(self) -> bool:
        return self.length == self.MAX
        