from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import *

def test_same_length_tree():
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
    bt2.root.left.right = Node(6)
    bt2.root.right.right = Node(9)
    bt2.root.left.right.left = Node(5)
    bt2.root.left.right.right = Node(20)
    bt2.root.right.right.left = Node(4)

    expected = [2, 7, 5, 6, 9, 5, 4]
    actual = tree_intersection(bt1,bt2)
    assert expected == actual

def test_diffrent_length_tree():
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


    expected = [2, 7, 5]
    actual = tree_intersection(bt1,bt2)
    assert expected == actual


def test_with_empty_tree():
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


    expected = []
    actual = tree_intersection(bt1,bt2)
    assert expected == actual
