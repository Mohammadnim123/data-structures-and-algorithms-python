from data_structures_and_algorithms.data_structures.tree.tree import Node,BinaryTree,BinarySearchTree

def find_maximum_value(tree):
        
    """
    find maximum value in tree
    """
    def _max_value(any_list):
        try:
            
            x = any_list[0]
            for i in any_list:
                if i > x:
                    x=i
            return x

        except:
            raise ValueError("empty tree !!")
    
    output = tree.preOrder()
    return _max_value(output)
    


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

    bb = BinaryTree()

    print(find_maximum_value(bb))
    
