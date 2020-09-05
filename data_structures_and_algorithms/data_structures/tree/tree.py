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



if __name__=='__main__':
    mohd = BinarySearchTree()
    mohd.add(1)
    mohd.add(2)
    mohd.add(3)
    mohd.add(4)
    mohd.add(5)
    
    print(mohd.postOrder())
    print(mohd.inOrder())
    print(mohd.preOrder())