from data_structures_and_algorithms.data_structures.tree.tree import *

def breadth_first(tree):
    """
    it will return a list of the values in the tree in the order they were encountered.

    """
    try:
        temp_list = []
        results = []
        if not tree.root:
            return 'empty tree'
        else:    
            if tree.root:
                temp_list.append(tree.root)
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

    print(breadth_first(bt))