class Node:
    def __init__(self, value:int) -> None:
        self.value = value
        self.next = None
        self.prev = None

class Doubly_linkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def traverse(self) -> None:
        if self.length == 0:
            print(self.length, ' nodes to traverse')
            return None
        if self.length == 0: print(self.length, ' node')
        else: print(self.length, ' nodes')
        current = self.head
        while current:
            print(current.value, '-> ', end="")
            current = current.next
        print()

    def append(self, value:int) -> bool:
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return True

    def pop(self) -> int:
        if self.length == 0:
            print(self.length, ' nodes to pop')
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepand(self, value:int) -> bool:
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        return True

    def pop_first(self) -> int:
        if self.length == 0:
            print(self.length, ' nodes to pop')
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def get_value(self, index;int) -> None:
        if index < 0 or index > self.length:
            print(index, ' is out or range')
            return None
        
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
                return current
        elif index > self.length / 2:
            temp = self.tail
            for _ in range(index):
                temp = temp.prev
        if temp is not None: return temp
        else: return None


mds = Doubly_linkedList()

mds.append(1)
mds.append(2)
mds.append(3)
mds.append(4)

mds.traverse()

mds.pop()

mds.traverse()

