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

def test_append_and_multiple_append():
    test = LinkedList()
    test.append(0)
    test.append(1)
    test.append(2)
    test.append(3)
    expected = "{ 0 } -> { 1 } -> { 2 } -> { 3 } -> { Null } -> "
    actual = test.__str__()
    assert expected == actual

def test_insertAfter_at_middle():
    test = LinkedList()
    test.append(0)
    test.append(1)
    test.append(2)
    test.append(3)
    test.insertAfter(1,'im middle')
    expected = "{ 0 } -> { 1 } -> { im middle } -> { 2 } -> { 3 } -> { Null } -> "
    actual = test.__str__()
    assert expected == actual

def test_insertAfter_at_last():
    test = LinkedList()
    test.append(0)
    test.append(1)
    test.append(2)
    test.append(3)
    test.insertAfter(3,'at last')
    expected = "{ 0 } -> { 1 } -> { 2 } -> { 3 } -> { at last } -> { Null } -> "
    actual = test.__str__()
    assert expected == actual

def test_insertBefore_at_first():
    test = LinkedList()
    test.append(0)
    test.append(1)
    test.append(2)
    test.append(3)
    test.insertBefore(0,'at_first')
    expected = "{ at_first } -> { 0 } -> { 1 } -> { 2 } -> { 3 } -> { Null } -> "
    actual = test.__str__()
    assert expected == actual

def test_insertBefore_at_middle():
    test = LinkedList()
    test.append(0)
    test.append(1)
    test.append(2)
    test.append(3)
    test.insertBefore(2,'at_middle')
    expected = "{ 0 } -> { 1 } -> { at_middle } -> { 2 } -> { 3 } -> { Null } -> "
    actual = test.__str__()
    assert expected == actual



