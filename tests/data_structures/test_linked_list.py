from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,
)


def test_instance():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


def test_empty():
    test = LinkedList()
    expected = None
    actual = print(test)
    assert expected == actual


def test_insert():
    test = LinkedList()
    test.insert(0)
    test.insert(1)
    test.insert(2)
    test.insert(3)
    expected = "{ 3 } -> { 2 } -> { 1 } -> { 0 } -> { Null } -> "
    actual = test.__str__()
    assert expected == actual
    

def test_includes():
    test = LinkedList()
    test.insert(0)
    test.insert(1)
    test.insert(2)
    test.insert(3)
    expected = True
    actual = test.includes(3)
    assert expected == actual
    
def test_head():
    test = LinkedList()
    test.insert(0)
    test.insert(1)
    test.insert(2)
    test.insert(3)
    assert test.head.value == 3
