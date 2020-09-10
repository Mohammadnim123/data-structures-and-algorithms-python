from data_structures_and_algorithms.data_structures.tree.tree import *

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self):
        try:    
            """
            Pre-order: root >> left >> right
            """
            output = []
            def _walk(node):
                if not node:
                    return
                output.append(node.value)
                _walk(node.left)
                _walk(node.right)
            _walk(self.root)
            return output
        except ValueError as e:
            print(f"error : {e}")



    def inOrder(self):
        try:    
            """
            In-order: left >> root >> right
            """
            output = []
            def _walk(node):
                if not node:
                    return
                _walk(node.left)
                output.append(node.value)
                _walk(node.right)
            _walk(self.root)
            return output
        except ValueError as e:
            print(f"error : {e}")

    def postOrder(self):
        """
        Post-order: left >> right >> root
        """
        try:
            output = []
            def _walk(node):
                if not node:
                    return
                _walk(node.left)
                _walk(node.right)
                output.append(node.value)
            _walk(self.root)
            return output
        except ValueError as e:
            print(f"error : {e}")  

    def breadth_first(self):
        """
        it will return a list of the values in the tree in the order they were encountered.

        """
        try:
            temp_list = []
            results = []
            if not self.root:
                return 'empty tree'
            else:    
                if self.root:
                    temp_list.append(self.root)
                while temp_list:
                    current = temp_list.pop(0)
                    results.append(current.value)
                    if current.left:
                        temp_list.append(current.left)
                    if current.right:
                        temp_list.append(current.right)
            return results
        except:
            raise ValueError('something wrong')    



class BinarySearchTree(BinaryTree):
    
    def add(self, value):
        """
        accepts a value, and adds a new node with that value in the correct location in the binary search tree. 
        """
        try:
            if not self.root:
                self.root = Node(value)
            else:
                current = self.root
                while (current):
                    if current.value > value: # Got to left
                        if current.left == None: # if current is a leaf
                            current.left = Node(value)
                            break
                        current = current.left
                    else:
                        if current.right == None: # if current is a leaf
                            current.right = Node(value)
                            break
                        current = current.right
        except ValueError as e:
            print(f"error : {e}")        
    
    
    def contains(self, value):
        """
        it accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once. 
        """
        try:
            if not self.root:
                return False
            else:
                current = self.root
                while (current):
                    if current.value==value:
                        return True
                    if current.value > value: 
                        if current.left == None: 
                            return False
                        current = current.left
                    else:
                        if current.right == None: 
                            return False
                        current = current.right
        except ValueError as e:
            print(f"error : {e}") 



if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.left = Node(7)
    bt.root.right = Node(5)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    bt.root.left.right.right = Node(11)
    bt.root.left.right.left = Node(5)

    print(bt.breadth_first())