from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList,Node
from data_structures_and_algorithms.challenges.ll_zip.ll_zip import zipLists

def test_equal_list():
    test1 = LinkedList()
    test2 = LinkedList()
    
    test1.append(1)
    test1.append(3)
    test1.append(2)
    
    test2.append(5)
    test2.append(9)
    test2.append(4)
    
    zipLists(test1,test2)
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> { Null } -> "
    actual = test1.__str__()
    assert expected == actual

def test_not_equal_list_1():
    test1 = LinkedList()
    test2 = LinkedList()
    
    test1.append(1)
    test1.append(3)
    
    
    test2.append(5)
    test2.append(9)
    test2.append(4)
    
    zipLists(test1,test2)
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> { Null } -> "
    actual = test1.__str__()
    assert expected == actual

def test_not_equal_list_2():
    test1 = LinkedList()
    test2 = LinkedList()
    
    test1.append(1)
    test1.append(3)
    test1.append(2)
    
    
    test2.append(5)
    test2.append(9)
    
    
    zipLists(test1,test2)
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { Null } -> "
    actual = test1.__str__()
    assert expected == actual