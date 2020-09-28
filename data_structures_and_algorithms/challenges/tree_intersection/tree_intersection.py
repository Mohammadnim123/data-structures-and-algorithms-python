from data_structures_and_algorithms.challenges.breadth_first.breadth_first import *

def tree_intersection(tree1,tree2):
    arr1 = breadth_first(tree1)
    arr2 = breadth_first(tree2)
    result = []

    my_len = len(arr1)
    if len(arr1)>len(arr2):
        my_len = len(arr2)
    
    for i in range(0,my_len):
        if arr1[i] == arr2[i]:
            result.append(arr1[i])

    return result



if __name__ == "__main__":
    bt1 = BinaryTree()
    bt1.root = Node(2)
    bt1.root.left = Node(7)
    bt1.root.right = Node(5)
    bt1.root.left.left = Node(2)
    bt1.root.left.right = Node(6)
    bt1.root.right.right = Node(9)
    bt1.root.left.right.left = Node(5)
    bt1.root.left.right.right = Node(11)
    bt1.root.right.right.left = Node(4)


    bt2 = BinaryTree()
    bt2.root = Node(2)
    bt2.root.left = Node(7)
    bt2.root.right = Node(5)
    bt2.root.left.left = Node(5)


    print(tree_intersection(bt1,bt2))
