from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks import *

def test_single_enqueue():
    test = PseudoQueue()
    test.enqueue(5)
    expected = 5
    actual = test.rear
    assert expected == actual

def test_multiple_enqueue():
    test = PseudoQueue()
    test.enqueue(5,6,7,8)
    expected = 8
    actual = test.rear
    assert expected == actual

def test_dequeue():
    test = PseudoQueue()
    test.enqueue(5,6,7,8)
    expected = 5
    actual = test.dequeue()
    assert expected == actual

def test_dequeue_from_empty():
    test = PseudoQueue()
    expected = 'empty queue !!!'
    actual = test.dequeue()
    assert expected == actual
    