from data_structures_and_algorithms.challenges.fizz_buzz_tree.fizz_buzz_tree import *
import pytest

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
    test.root.left.right.left = Node(15)    
    expected = ['2', '7', 'Buzz', '2', 'Fizz', 'Fizz', 'FizzBuzz', '11', '4']
    actual = breadth_first(fizz_buzz_tree(test))
    assert expected == actual

def test_empty_tree():
    test = BinaryTree()
    expected = 'empty tree'
    actual = breadth_first(fizz_buzz_tree(test))
    expected == actual


    

def test_tree_with_minus():
    test = BinaryTree()
    test.root = Node(-2)
    test.root.left = Node(-7)
    test.root.right = Node(-5)
    test.root.left.left = Node(-2)
    test.root.left.right = Node(-6)
    test.root.right.right = Node(-9)
    test.root.right.right.left = Node(-4)
    test.root.left.right.right = Node(-15)
    test.root.left.right.left = Node(0)
    expected = ['-2', '-7', 'Buzz', '-2', 'Fizz', 'Fizz', 'FizzBuzz', 'FizzBuzz', '-4']
    actual = breadth_first(fizz_buzz_tree(test))
    assert expected == actual


def test_tree_with_one_value():
    test = BinaryTree()
    test.root = Node(5)
    expected = ['Buzz']
    actual = breadth_first(fizz_buzz_tree(test))
    assert expected == actual

def test_error():
    test = 'mohammad'
    with pytest.raises(ValueError):
        fizz_buzz_tree(test)

