from data_structures_and_algorithms.challenges.breadth_first.breadth_first import * 
import pytest

def test_empty_tree():
    test = BinaryTree()
    expected = 'empty tree'
    actual = test.breadth_first()
    expected == actual

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

    expected = [2,7,5,2,6,9,5,11,4]
    actual = test.breadth_first()
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

    expected = [-2,-7,-5,-2,-6,-9,0,-11,-4]
    actual = test.breadth_first()
    assert expected == actual

def test_tree_with_one_value():
    test = BinaryTree()
    test.root = Node(5)
    expected = [5]
    actual = test.breadth_first()
    assert expected == actual


    