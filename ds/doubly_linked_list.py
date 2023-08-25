class Node:
    def __init__(self, data):
        self.data = data
        self.prev_ref = None
        self.next_ref = None

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is not None:
            n = self.head
            while n is not None:
                print(f"{n.data} ---> ", end="")
                n = n.next_ref
            print("")
    
    def traverse_reverse(self):
        if self.head is not None:
            n = self.head
            while n.next_ref is not None:
                n = n.next_ref
            while n is not None:
                n = n.prev_ref
                print(f"{n.data} ---> ", end="")

    def add_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next_ref = self.head
            self.head = node

    def add_after(self, data, after_of):
        if self.head is not None:
            node = Node(data)
            n = self.head
            while n.next_ref is not None:
                if n.data == after_of:
                    break
                n = n.next_ref
            node.next_ref = n.next_ref
            n.next_ref = node

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            n = self.head
            while n.next_ref is not None:
                n = n.next_ref
            node.prev_ref = n
            n.next_ref = node
    
    def size(self):
        if self.head is None:
            return 0
        else:
            count = 1
            n = self.head
            while n.next_ref is not None:
                n = n.next_ref
                count += 1
            return count

    def get(self, position):
        if self.head is not None and position < self.size():
            n = self.head
            idx = 0
            while idx < position:
                n = n.next_ref
                idx += 1
            return n
        else: return f"{position} position is not available in the {self.size()} lenght list"

    def pop(self):
        if self.head is not None:
            n = self.head
            while n.next_ref is not None:
                if n.next_ref.next_ref is None:
                    break
                else:
                    n = n.next_ref
            popped = n.next_ref
            n.next_ref = None
            return popped

    def delete(self, value):
        if self.head is not None:
            n = self.head
            while n.next_ref is not None:
                if n.data == value:
                    break
                n = n.next_ref
            if n.next_ref is not None:
                n.next_ref.prev_ref = n.prev_ref
                n.prev_ref.next_ref = n.next_ref
            
        if self.head.next_ref is None: 
            if self.head.data == value:
                self.head = None

dll = DoublyLinkedList()
dll.add(1)
dll.add(2)
dll.add(3)
dll.add(4)
dll.add_after('X', 2)
dll.traverse()
print(dll.size())
dll.pop()
dll.pop()
dll.delete_by_value('X')
dll.traverse()
print(dll.size())
