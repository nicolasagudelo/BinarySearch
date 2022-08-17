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

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(f'Depth = {self.depth}, Value = {self.value}')
        if self.right:
            self.right.inorder_traversal()
    
    def preorder_traversal(self):
        print(f'Depth = {self.depth}, Value = {self.value}')
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(f'Depth = {self.depth}, Value = {self.value}')

    def minValueNode(self):
        while(self.left is not None):
            self = self.left
  
        return self

    def deleteNode(self, value):

        if self is None:
            return self
    
        if value < self.value:
            self.left = self.left.deleteNode(value)
    
        elif(value > self.value):
            self.right = self.right(value)
    
        else:
    
            if self.left is None:
                return self.right
    
            elif self.right is None:
                return self.left
                
            temp = self.right.minValueNode()
    
            # Copy the inorder successor's 
            # content to this node
            self.value = temp.value
    
            # Delete the inorder successor
            self.right = self.right.deleteNode(temp.value)
    
        return self
            


self = BinarySearchTree(100)
self.insert(50)
self.insert(125)
self.insert(75)
self.insert(25)

print('\t\t',self.value,'\n')
print('\t',self.left.value, '\t\t', self.right.value)
print(self.left.left.value, '\t\t',self.left.right.value)

print(self.get_node_by_value(125).value)
print(self.get_node_by_value(124))

print('INORDER:')
self.inorder_traversal()
print('PREORDER:')
self.preorder_traversal()
print('POSTORDER:')
self.postorder_traversal()

self.deleteNode(50)

print('INORDER AFTER DELETE:')
self.inorder_traversal()
print('PREORDER AFTER DELETE:')
self.preorder_traversal()
print('POSTORDER AFTER DELETE:')
self.postorder_traversal()