class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

        self.array = []

    def traverse(self) -> None:
        if self.length == 0:
            print(f"{self.length} node to traverse")
            return None

        current = self.head
        while current:
            print("N: ", current.value, "-> ", end="")
            current = current.next
        print()

    def show_array(self) -> list:
        if self.length == 0 and len(self.array) == 0:
            print(f"No nodes to in the array")
            return None

        for node in self.array:
            print("A: ", node.value, "-> ", end="")
        print()

        return self.array

    def append(self, value: int) -> bool:
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.array.append(node)
        else:
            self.tail.next = node
            self.tail = node
            self.array.append(node)
        self.length += 1
        return True

    def pop(self) -> object:
        if self.length == 0:
            print(f"{self.length} nodes to pop")
            return None

        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.array.pop()
        else:
            temp = self.array[-2]
            self.array.pop()
            self.tail = temp
            self.tail.next = None
        self.length -= 1
        return temp

    def get(self, index: int) -> object:
        if index < 0 or index > self.length or index > len(self.array):
            print("Index out of bounds")
            return False
        # print(f"Testing: {self.length}")
        # print(f"Testing: {len(self.array)}")
        if index == self.length:
            return self.array[index]
        return self.array[index]

    def set(self, index: int, value: int) -> bool:
        if index < 0 or index > self.length or index > len(self.array):
            print("Index out of bounds")
            return False
        if index == self.length:
            return self.append(value)
        if self.length == 0:
            print(f"{self.length} nodes")
            return False
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def reverse(self) -> None:
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            tmep = after

    def middleNode(self) -> object:
        if self.length == 0:
            return None
        middle, steptwo = self.head
        while steptwo.next:
            middle = middle.next
            steptwo = steptwo.next.next
        return middle

    def has_loop(self) -> bool:
        if self.length == 0:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def move_node_to_end(self, node: object) -> None:
        if self.length == 0:
            return None

        dummy1 = Node(0)
        batch = dummy1
        current = self.head

        pre = None
        while current:
            if current.value == node:
                batch.next = node
                bacth = node

                pre.next = current.next
            else:
                pre = current
            current = current.next
        batch.next = None
        self.head = batch.next
