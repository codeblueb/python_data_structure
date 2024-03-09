class Node:
    def __init__(self, value: node) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init_(self, value=None) -> None:
        if not value:
            self.head = None
            self.tail = None
        else:
            self.value = value
            self.tail = value
        self.length = 0

        def traverse(self, behavior: str) -> None:
            """
            Function: Two sets of behaviors
                        - frombottom
                        - topbottom
            frombottom: this will reverse the linked list then print the linked stack
            topbottom:  this will print the linkedlist as is
            """
            if self.length == 0:
                print(f"{self.length} nodes to traverse")
                return None
            if behavior == "frombottom":
                self.traverse()
                current = self.head
                while current:
                    print(current.value, "-> ", end="")
                print()
            elif behavior == "topbottom":
                current = self.head
                while current:
                    print(current.value, "-> ", end="")
                print()

        def prepand(self, value: node) -> bool:
            node = Node(value)
            if self.lenth == 0:
                self.head = node
                self.tail = node
            else:
                node.next = self.head
                self.head = node
            self.length += 1
            return True

        def pop_first(self) -> object:
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

        def traverse(self) -> None:
            if self.length > 2:
                temp = self.head
                self.head = self.tail
                self.tail = temp

                before = None
                for _ in range(self.length):
                    after = temp.next
                    temp.next = before
                    before = temp
                    temp = after
            else:
                return None
