class Node:
    def __init__(self, value:int) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def traverse(self) -> None:
        node = self.head
        if self.length >= 1:
            print(self.length, ' node')
            while node:
                print(node.value, '-> ', end='')
                node = node.next
            print()

    def empty() -> bool:
        if self.length == 0:
            return True
        else: return False

    def append(self, value:int) -> None:
        """Add a node @ O(1)"""
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    def pop(self) -> object:
        """pop a node from the end @ O(n)"""
        if self.length == 0:
            print(self.length, ' nodes to pop')
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            pre = None
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        return temp

    def prepand(self, value:int) -> bool:
        """Add a node from the front @ O(1)"""
        node = Node(value)
        if self.length == 1:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return True

    def pop_first(self) -> object:
        """Pop an item from the front @ O(1)"""
        if self.length == 0:
            print(self.length, ' nodes to pop')
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

    def get_value(self, index:int) -> object:
        """Get the node @ O(n) CAN WE DO BETTER ??!!"""
        if index < 0 or index > self.length:
            print(index, ' out of range')
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        if current is not None:
            return current
        else:
            return None

    def set_value(self, index:int, value:int) -> bool:
        """Set the node with new value @ O(n) CAN WE DO BETTER ??!!"""
        if index < 0 or index < self.length:
            print(index, ' out of range')
            return False
        node = self.get_value(index)
        if node is not None:
            node.value = value
            return True
        else:
            return False

    def insert(self, index:int, value:int) -> bool:
        """Add a node to a given index @ O(n) CAN WE DO BETTER ??!!"""
        if index < 0 or index > self.length:
            print(index, ' out of range')
            return False
        if index == 0: return self.prepand(value)
        if index == self.length: return self.append(value)

        node = Node(value)
        pre = self.get_value(index-1)
        node.next = pre.next
        pre.next = node
        self.length += 1
        return True

    def remove(self, index:int) -> object:
        """Remove a node given a index @ O(n) CAN WE DO BTTER??!!"""
        if index < 0 or index > self.length:
            print(index, ' out of range')
            return None
        if index == 0: return self.pop_first()
        if index == self.length: return self.pop()
        
        pre = self.get_value(index-1)
        temp = temp.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self) -> None:
        """Reverse the linkedlist"""
        if self.length > 1:
            temp = self.head
            self.head = self.tail
            self.tail = temp
            before = None
            for _ in range(self.length):
                after = temp.next
                temp.next = before
                before = temp
                temp = after
        else: print(self.length, ' nodes,\nNeed more than 1 node')

    def find_middle_node(self) -> object:
        if self.length > 3:
            middle = steptwo = self.head
            while steptwo and steptwo.next:
                middle = middle.next
                steptwo = steptwo.next.next
            return middle

    def has_loop(self) -> bool:
        """Check the linkedlist to see if it has a LOOP @ O(n)"""
        if self.length == 0:
            return False
        slow = self.head
        fast = slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def find_kth_from_end(self, k:int) -> object:
        """Find node at given index from the end @ O(n)"""
        if k < 0 or k > self.length:
            print(k, ' out of range')
            return None
        slow = fast = self.head
        while fast and fast.next:
            if fast is None: return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def partition(self, x:int) -> None:
        if self.length > 3:

            dum1 = Node(0)
            dum2 = Node(0)
            less = dum1.next
            more = dum2.next
            current = self.head

            while current:
                if current.value < x:
                    less.next = current
                    less = current
                else:
                    more.next = current
                    more = current
                current = current.next
            less.next = None
            more.next = None
            less.next = dum2.next
            self.head = dum1.next
        else: print("Need more than 3 nodes")

    def remove_duplicates(self) -> None:
        if self.length == 0:
            print(self.length, ' nodes')
            return None
        unq = set()
        current = self.head
        pre = None
        while current:
            if current.value in unq:
                pre.next = current.next
                self.length -= 1
            else:
                pre = current
            current = current.next

    def move_zeros_to_end(self) -> None:
        if self.length == 0: return None
    
        dum1 = Node(0)
        zeros = dum1.next
        current = self.head
        pre = None
        while current:
            if current == 0:
                zeros.next = current
                zeros = current
                pre.next = current.next
            else:
                pre = current
            current = current.next
        zeros.next = None
        pre.next = dum.next

    def binary_to_decimal(self) -> int:
        if self.length == 0: return None
        current = self.head
        decimal = 0
        while current:
            decimal  = decimal * 2 + current.value
            current = current.next
        return decimal

    def reverse_between(self, start_index, end_index) -> None:
        if start_index < 0 and end_index > self.length:
            print(start_index, end_index, ' both index out of range')
            return None
        
        dum = Node(0)
        dum.next = self.head
        pre = dum
        for _ in range(start_index):
            pre = pre.next
        current = pre.next
        for _ in range(end_index-start_index):
            after = current.next
            current.next = after.next
            after.next = pre.next
            pre.next = after
        self.head = dum.next

def match_1_instruction(obj, cmd):
    match cmd:
        case 'pop':
            obj.pop()
        case 'pop-first':
            obj.pop_first()
        case 'reverse':
            obj.reverse()
        case 'find-middle-node':
            node = obj.find_middle_node()
            if node: print(node.value)
            elif obj.empty(): print("Empty linked list")
            else: print("No middle node found")
        case 'has-loop':
            check = obj.has_loop()
            if check: print("The linked list has a loop")
            else: print("The linked list does not have a loop")
        case 'move-zeros':
            obj.move_zeros_to_the_end()
        case 'binary-to-decimal':
            obj.binary_to_decimal()
        case 'remove-duplicates':
            obj.remove_duplicates()

def match_2_instruction(obj, cmd, value):
    match cmd:
        case 'append':
            if value.isdigit():obj.append(int(value))
            else:obj.append(value)
        case 'prepand':
            if value.isdigit():obj.prepend(int(value))
            else:obj.prepand(value)
        case 'get-value':
            if value.isdigit():
                node = obj.get_value(int(value))
                print(node.value)
        case 'remove':
            if value.isdigit():
                obj.remove(int(value))
        case 'find-kth-from-end':
            if value.isdigit():
                node = obj.find_kth_from_end(int(value))
                if node: print(node.value)
        case 'partition':
            if value.isdigit():
                obj.partition(int(value))
                obj.traverse()

def match_3_instruction(obj, cmd, index, value):
    match cmd:
        case 'insert':
            if index.isdigit():
                if value.isdigit():obj.insert(int(index),int(value))
                else:obj.insert(int(index), value)
        case 'set-value':
            if index.isdigit():
                if value.isdigit():obj.set_value(int(index), int(value))
                else:obj.set_value(int(index), value)
        case 'reverse-between':
            if index.isdigit() and value.isdigit():
                obj.reverse_between(int(index), int(value))

mds = LinkedList()

while True:
    print("What do you want to do?\nType no exit...")
    ask = None
    ask = input("> ")
    if ask.lower() == 'no':break
    if ask.lower() in ['pop', 'pop-first', 'reverse', 'find-middle-node', 'has-loop',
                       'move-zeros', 'binary-to-decimal', 'remove-duplicates']:
        match_1_instruction(mds, ask.lower())

    if ask.lower().rsplit(' ')[0] in ['append', 'prepand', 'get-value', 'remove',
                                      'find-kth-from-end', 'partition']:
        user_tokens = ask.lower().rsplit(' ')
        if len(user_tokens) > 2:
            print("Too many arguments")
            break
        match_2_instruction(mds, user_tokens[0], user_tokens[1])

    if ask.lower().rsplit(' ')[0] in ['insert', 'set-value', 'reverse-between']:
        user_tokens = ask.lower().rsplit(' ')
        if len(user_tokens) > 3:
            print("Too many arguments")
            break
        match_3_instruction(mds, user_tokens[0], user_tokens[1], user_tokens[2])
    print('----------------------')
    mds.traverse()


# from dataclasses import dataclass
# import sys
# class Emptystr(Exception):
#
#     def __init__(self, message: str):
#         self.message = message # the only reason you want to do this is to use it
#         super(Emptystr, self).__init__(message)
#
# class EmptyLinkedList(Exception):
#
#     def __init__(self, message: str):
#         self.message = message
#         super(EmptyLinkedList, self).__init__(message)
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# class LinkedList:
#
#     def __init__(self, value):
#         node = Node(value)
#         self.head = node
#         self.tail = node
#         self.length = 1
#
#     def traverse(self):
#         if self.length != 0:
#             temp = self.head
#             print(f"{self.length} node")
#             print('----------')
#             while temp:
#                 print(temp.value)
#                 temp = temp.next
#         else:return None # nothing to traverse
#
#     def append(self, value):
#         """
#         The idea is to check if there is a linked list with atleat one node
#         then append if there isnt any else
#         point the tail to next and make tail the new node
#
#         O(1) : because we have to point the tail.next to the new ndoe
#         """
#         if isinstance(value, str):
#             if value == "":raise Emptystr("Creating a empty string node is not allowed")
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True
#
#     def pop(self):
#         """
#         The idea is to make sure there is something pop and then
#         iterate through temp by pointing to the head and holding a previous pointer
#         and upon reaching to the end previous will be pointing to the previous node
#         and not the last so once that happens we point the tail to the previous and
#         then set the tail.next to None to let go of the last node
#
#         O(n)
#         """
#         if self.length == 0: raise EmptyLinkedList('Nothing to pop...')
#         temp = self.head
#         pre = self.head
#         while temp.next:
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         print(self.length)
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
#
#     def prepand(self, value):
#         """
#         The idea is to make sure we are not creating an empty node and then
#         check if the linked list exist by checking for length if 0 then
#         go ahead and create the first node else make the new node point
#         the next then make the head point to the new node
#
#         O(1) because we are just instructing a node by maniplating the first pointer
#         """
#         if isinstance(value, str):
#             if value == "":raise Emptystr("Creating a empty string node is not allowed")
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
#         return True
#
#     def pop_first(self):
#         """
#         The idea is to check for the length of the linked list and then
#         create a pointer to the head and then make the self.head -> self.head.next
#         then get rid of the temp
#         """
#         if self.length == 0: raise EmptyLinkedList('Nothing to pop...')
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#
#     def get_value(self, index):
#         """
#         The idea is to get the value based on the index but check for if the index
#         is less than 0 or if the index is greater than self.length
#         then iterate through the list until you reach the index and then return the value
#
#         O(n)
#         """
#         if index < 0 or index > self.length: return None
#         if self.length == 0: raise EmptyLinkedList('Nothing to get')
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp
#
#
#     def set_value(self, index, value):
#         """
#         The idea is to make sure the index is valid by checking with class length and making
#         that the index is not -1 and then using the get_value method we can use to get the
#         node at the given index and if the node is not None then you set the value to that node
#
#         O(n)
#         """
#         if index < 0 or index > self.length: return False
#         if self.length == 0: raise EmptyLinkedList('There is nothing to set')
#         temp = self.get_value(index)
#         if temp is not None:
#             temp.value = value
#             return True
#         return False
#
#     def insert(self, index, value):
#         """
#         The idea is to make sure the index is valid by checking with class length and
#         making that the index is not -1 and then if the index is 0 then use the method
#         to prepand with given index or if the index is equal to class length the use appned
#         else create a new node then use the get_value method with index -1 the set the new_node.next
#         to temp.next that we get from using the get_value method finaly set the temp.next to new_node
#
#         O(n)
#         """
#         if index < 0 or index > self.length: return False
#         if index == 0: return self.prepand(value)
#         if index == self.length: return self.append(value)
#
#         new_node = Node(value)
#         temp = self.get_value(index-1)
#         new_node.next = temp.next
#         temp.next = new_node
#         self.length += 1
#         return True
#
#     def remove(self, index):
#         """
#         The idea is to remove a node by a given index but make sure the index is a valid
#         greater than 0 if not 0 and less than the length of the list then if it is 0 run the
#         pop first method or if the index is equal to class length then use the pop method
#         else then get the prev node of the index -1 using get_value method then
#         create a temp node pointing to the previous node.next then make the prev.next
#         point to the temp.next finally make the temp set to None and decrement
#
#         O(n)
#         """
#         if index < 0 or index > self.length: return None
#         if index == 0: return self.pop_first()
#         if index == self.length: return self.pop()
#
#         prev_node = self.get_value(index-1)
#         temp = prev_node.next
#         prev_node.next = temp.next
#         temp.next = None
#         self.length -= 1
#         return True
#
#
#     def reverse(self):
#         """
#         The idea is to hold a temp for the head before setting the head to tail and tail to head
#         then create a afer and before by setting after to the head the next and before to None
#         then iterate and set after to head.next then head.next to before and make sure
#         set before to temp before setting temo back to after
#         """
#         temp = self.head
#         self.head = self.tail
#         self.tail = temp
#         after = temp.next
#         before = None
#         for _ in range(self.length):
#             after = temp.next
#             temp.next = before
#             before = temp
#             temp = after
#
#
# def match_1_instruction(obj, cmd):
#     match cmd:
#         case 'pop':
#             obj.pop()
#         case 'pop-first':
#             obj.pop_first()
#         case 'reverse':
#             obj.reverse()
#
# def match_2_instruction(obj, cmd, value):
#     match cmd:
#         case 'append':
#             obj.append(value)
#         case 'prepand':
#             obj.prepand(value)
#         case 'get-value':
#             if value.isdigit():
#                 node = obj.get_value(int(value))
#                 print(node.value)
#         case 'remove':
#             if value.isdigit():
#                 obj.remove(int(value))
# def match_3_instruction(obj, cmd, index, value):
#     match cmd:
#         case 'insert':
#             if index.isdigit():
#                 obj.insert(int(index), value)
#         case 'set-value':
#             if index.isdigit():
#                 obj.set_value(int(index), value)
#
# linkedlist = LinkedList('WARNING')
# linkedlist.traverse()
#
# while True:
#     print("What do you want to do?")
#     ask = None
#     ask = input("> ")
#     if ask.lower() == 'no':break
#     if ask.lower() in ['pop', 'pop-first', 'reverse']:
#         match_1_instruction(linkedlist, ask.lower())
#
#     if ask.lower().rsplit(' ')[0] in ['append', 'prepand', 'get-value', 'remove']:
#         user_tokens = ask.lower().rsplit(' ')
#         if len(user_tokens) > 2:
#             print("Too many arguments")
#             break
#         match_2_instruction(linkedlist, user_tokens[0], user_tokens[1])
#
#     if ask.lower().rsplit(' ')[0] in ['insert', 'set-value']:
#         user_tokens = ask.lower().rsplit(' ')
#         if len(user_tokens) > 3:
#             print("Too many arguments")
#             break
#         match_3_instruction(linkedlist, user_tokens[0], user_tokens[1], user_tokens[2])
#     print('----------------------')
#     linkedlist.traverse()
#


         



