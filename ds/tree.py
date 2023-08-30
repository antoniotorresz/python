class BinarySearchTree:
    def __init__(self, key=None):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self, data):
        if self.key is None:#means tree is empty
            self.key = data
            return
        if self.key == data:#ignoring duplicated 
            return
        #check the position of the node left or right
        if self.key > data:#right now is inserting to the right due de grather than simbol, if want to insert to left just change to >=
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BinarySearchTree(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BinarySearchTree(data)

    def search(self, data):
        if self.key == data:
            print('found!')
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('not present')
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('not present')

    def traverse_pre_order(self):
        print(self.key, end=' ')
        if self.lchild:
            self.lchild.traverse_pre_order()
        if self.rchild:
            self.rchild.traverse_pre_order()

    def traverse_in_order(self):
        if self.lchild:
            self.traverse_in_order()
        print(self.key)
        if self.rchild:
            self.traverse_in_order()

    def traverse_post_order(self):
        if self.lchild:
            self.lchild.traverse_post_order()
        if self.rchild:
            self.rchild.traverse_post_order()
        print(self.key, end=' ')

    def delete(self, data):
        pass
root = BinarySearchTree()

numbers = [20, 4, 30, 4, 1, 5, 6]
for n in numbers:
    root.insert(n)
root.search(100)
print('pre order traverse:')
root.traverse_pre_order()
print('')
print('post order traverse:')
root.traverse_post_order()
print('')