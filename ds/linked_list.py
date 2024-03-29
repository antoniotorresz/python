from pprint import pprint

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

    def __str__(self):
        return f"Node: {self}, data: {self.data}"

class LinkedList:
    def __init__(self):
        self.head = None #initially will be empty

    def to_string(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(f'[{n.data}] --> ', end="")
                n = n.ref
            print("")

    def add_start(self, data):
        node = Node(data)
        node.ref = self.head
        self.head = node

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            n = self.head
            while(n.ref is not None):
                n = n.ref
            n.ref = node
    
    def add_in_position(self, data, position):
        if position == 0:
            self.add_start(data)
        else:
            node = Node(data)
            idx = 1
            n = self.head
            while(idx < position):
                n = n.ref
                idx += 1
            next_node = n.ref
            n.ref = node
            node.ref = next_node

    def add_after(self, data, after_of):
        node = Node(data)
        if self.head is not None:
            n = self.head
            while(n.ref is not None):
                if n.data == after_of:
                    break
                else:
                    n = n.ref
            next = n.ref
            n.ref = node
            node.ref = next

    def add_before(self, data, before_of):
        node = Node(data)
        if self.head is not None:
            n = self.head
            while n.ref is not None:
                if n.ref.data == before_of:
                    break
                else:
                    n = n.ref
            node.ref = n.ref
            n.ref = node
            
    def remove_from_begin(self):
        if self.head is not None:
            self.head = self.head.ref
    
    def remove_with_value(self, value):
        if self.head is not None:
            if self.head.data == value:
                self.head = self.head.ref
                return
            
            n = self.head
            while n.ref is not None:
                if n.ref.data == value:
                    break
                else:
                    n = n.ref
            n.ref = n.ref.ref

    def pop(self):
        if self.head is not None:
            n = self.head
            while n.ref is not None:
                if n.ref.ref is None:
                    last = n.ref
                    n.ref = None
                    return last
                else:
                    n = n.ref

    def clean(self):
        self.head = None
    
    def size(self):
        if self.head is None:
            return 0
        else:
            count = 1
            n = self.head
            while(n.ref is not None):
                n = n.ref
                count += 1
            return count

ll = LinkedList()
ll.add_start("Hello")
ll.add_start(2)
ll.add_start(3434)
ll.add(0)
ll.add(1)
ll.add_in_position('x', 1)
ll.add_after(10e6, 'Hello')
ll.add_before(-10e3, 'x')
print(f'size of the list: {ll.size()}')
ll.to_string()
print("removing first element in list")
ll.remove_from_begin()
ll.to_string()
print("removing last element")
ll.pop()
ll.to_string()
print("removing value")
ll.remove_with_value("Hello")
ll.remove_with_value(0)
ll.remove_with_value(-10e3)
ll.to_string()