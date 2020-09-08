from data_structures_and_algorithms.data_structures.tree.tree import *
from data_structures_and_algorithms.challenges.breadth_first.breadth_first import *

def fizz_buzz(value):
    """Function to do the fizz_buzz on the given value"""
    if value % 15 == 0:
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    else:
        return str(value)

def fizz_buzz_tree(tree):
    """Function to change all values in the given tree according to fizz_buzz """
    try:
        new_tree = BinaryTree()

        if not tree.root:
            return new_tree

        def helper(current):
            """Helper function to use in recurtion to add new values in the new_tree according to their positions in the original tree"""
            node = Node(fizz_buzz(current.value))

            if current.left:
                node.left = helper(current.left)
            if current.right:
                node.right = helper(current.right)
            return node


        new_tree.root = helper(tree.root)
        return new_tree

    except:
        raise ValueError('your input not tree')

    




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
    

    
    print(breadth_first(fizz_buzz_tree(bt)))


