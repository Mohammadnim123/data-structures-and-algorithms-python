from data_structures_and_algorithms.challenges.find_maximum_binary_tree.find_maximum_binary_tree import Node,BinaryTree,BinarySearchTree,find_maximum_value
import pytest

def test_empty_tree():
    test = BinaryTree()
    with pytest.raises(ValueError):
        find_maximum_value(test)

def test_full_tree():
    test = BinaryTree()
    test.root = Node(2)
    test.root.left = Node(7)
    test.root.right = Node(5)
    test.root.left.left = Node(2)
    test.root.left.right = Node(6)
    test.root.right.right = Node(9)
    test.root.right.right.left = Node(4)
    test.root.left.right.right = Node(11)
    test.root.left.right.left = Node(5)

    expected = 11
    actual = find_maximum_value(test)
    assert expected == actual
    

def test_tree_with_minus():
    test = BinaryTree()
    test.root = Node(-2)
    test.root.left = Node(-7)
    test.root.right = Node(-5)
    test.root.left.left = Node(-2)
    test.root.left.right = Node(-6)
    test.root.right.right = Node(-9)
    test.root.right.right.left = Node(-4)
    test.root.left.right.right = Node(-11)
    test.root.left.right.left = Node(0)

    expected = 0
    actual = find_maximum_value(test)
    assert expected == actual

def test_tree_with_one_value():
    test = BinaryTree()
    test.root = Node(5)
    expected = 5
    actual = find_maximum_value(test)
    assert expected == actual


