class Node:
    def __init__(self, value: node) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value: node) -> None:
        self.head = value
        self.tail = value
        self.length = 0

    def traverse(self) -> None:
        if self.length == 0:
            print(f"{self.length} nodes to traverse")
            return None
        current = self.head
        while current:
            print(current.value, "-> ", end="")
        print()

    def append(self, value: node) -> bool:
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    def pop_first(self) -> Object:
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None
        self.length -= 1
        return temp

    def show_lastnode(self) -> object:
        return self.tail

    def show_firstnode(self) -> Object:
        return self.head
