class BinarySearchTree:
    def __init__(self, value, depth = 1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value, self.depth + 1)
                print(f'Tree value {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value, self.depth + 1)
                print(f'Tree value {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):
        if self.value == value:
            return self
        if value > self.value and self.right:
            return self.right.get_node_by_value(value)
        if value < self.value and self.left:
            return self.left.get_node_by_value(value)

        return 'Value not found'

root = BinarySearchTree(100)
root.insert(50)
root.insert(125)
root.insert(75)
root.insert(25)

print('\t\t',root.value,'\n')
print('\t',root.left.value, '\t\t', root.right.value)
print(root.left.left.value, '\t\t',root.left.right.value)

print(root.get_node_by_value(125).value)
print(root.get_node_by_value(124))
