class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        head = self.head
        if self.length == 0: return
        while head.next:
            print(self.head.value)
            head = head.next
        

    def get(self, index: int) -> int:
        head = self.head
        while head and index:
            index -= 1
            head = head.next

        if index == 0 and head:
            print(head.value)
            return head.value
        return -1
        

    def addAtHead(self, val: int) -> None:
        obj = Node(val)
        if self.head:
            obj.next = self.head
            self.head = obj
        else:
            self.head = self.tail = obj
        self.length += 1


    def addAtTail(self, val: int) -> None:
        obj = Node(val)
        if self.head:
            self.tail.next = obj
            self.tail = obj
        else:
            self.head = self.tail = obj
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return
        head = self.head
        prev = None
        while head and index:
            index -= 1
            prev = head
            head = head.next

        if index == 0 and head:
            obj = Node(val)
            obj.next = head
            prev.next = obj
            self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            head = self.head
            self.head = head.next
            head.next = None
            self.length -= 1
            return

        head = self.head
        prev = None
        while head.next and index:
            index -= 1
            prev = head
            head = head.next

        if index == 0:
            prev.next = head.next
            self.length -= 1
            if not head.next:
                self.tail = prev
            head.next = None
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)