from data_structures_and_algorithms.challenges.linked_list.linked_list import Node,LinkedList

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
    expected = "{ 0 } -> { 1 } -> { 2 } -> { 3 } -> "
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
    assert test.head.value == 0



    