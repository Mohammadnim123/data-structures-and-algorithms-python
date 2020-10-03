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

    def pre_order(self, root=None, arr=None):
        """ Root left right """
        try:
            if arr == None:
                arr = []
            arr.append(root.value)
            if root.left:
                self.pre_order(root.left, arr)
            if root.right:
                self.pre_order(root.right, arr)
            return arr
        except AttributeError:
            return "A root element parameter is required"


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


    def new_add(self,value):
        if self.root == None:
            self.root = Node(value)
        
        curr = self.root
        while curr:
            if value < curr.value:
                if curr.left == None:
                    curr.left = Node(value)
                    break
                curr = curr.left

            else:
                if curr.right == None:
                    curr.right = Node(value)
                    break
                curr = curr.right
    

    
    
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

    def cont(self,value):
        curr = self.root
        if curr.value == value:
            return True
        while curr:
            if value == curr.value:
                return True
            elif value < curr.value:
                curr = curr.left
            elif value >curr.value:
                curr = curr.right
        return False

    def max_val_bs(self):
        
        if self.root == None:
            return None
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.value

    def max_val(self):
        try:    
            """
            Pre-order: root >> left >> right
            """
            maxx = [self.root.value]
            def _walk(node):
                
                if not node:
                    return
                if node.value > maxx[0]:
                    maxx[0] = node.value
                _walk(node.left)
                _walk(node.right)
            _walk(self.root)
            return maxx[0]
        except ValueError as e:
            print(f"error : {e}")        
            

 


if __name__=='__main__':
    tree = BinarySearchTree()
    tree.root = Node(2)
    tree.root.left = Node(70)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(20)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(9)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    
    # print(tree.postOrder())
    # print(tree.inOrder())
    print(tree.max_val())