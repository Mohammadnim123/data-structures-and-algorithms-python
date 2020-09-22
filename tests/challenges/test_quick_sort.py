from data_structures_and_algorithms.challenges.quick_sort.quick_sort import quick_sort


def test_simple_lst():
    lst = [8,4,23,42,16,15]
    quick_sort(lst, 0, 5)
    assert lst == [4, 8, 15, 16, 23, 42]

def test_list_reverse_order():
    lst = [42, 23, 16, 15, 8, 4]
    quick_sort(lst, 0, 5)
    assert lst == [4, 8, 15, 16, 23, 42]

def test_list_reverse_order2():
    lst = [20,18,12,8,5,-2]
    quick_sort(lst, 0, 5)
    assert lst == [-2, 5, 8, 12, 18, 20]

def test_list_zeros_and_negative():
    lst = [-23, -0.5, -4, 0, -1]
    quick_sort(lst, 0, 4)
    assert lst == [-23, -4, -1, -0.5, 0]

def test_few_uniques():
    lst = [5,12,7,5,5,7]
    quick_sort(lst, 0, 5)
    assert lst == [5, 5, 5, 7, 7, 12]

def test_nearly_sorted():
    lst = [2,3,5,7,13,11]
    quick_sort(lst, 0, 5)
    assert lst == [2, 3, 5, 7, 11, 13]

def test_sorted():
    lst = [2,3,5,7,11,13]
    quick_sort(lst, 0, 5)
    assert lst == [2,3,5,7,11,13]

def test_same_vals():
    lst = [1, 1, 1, 1, 1]
    quick_sort(lst, 0, 4)
    assert lst == [1, 1, 1, 1, 1]

def test_empty_list():
    lst = []
    quick_sort(lst, 0, 0)
    assert lst == []

def test_one_element():
    lst = [4]
    quick_sort(lst, 0, 0)
    assert lst == [4]

def test_two_elements():
    lst = [5, 4]
    quick_sort(lst, 0, 1)
    assert lst == [4, 5]

def test_strings():
    lst = ['cat','a', 'c', 'b']
    quick_sort(lst, 0, 3)
    assert lst == ['a', 'b', 'c', 'cat']

def test_another_lst():
    lst = [5,12,7,5,5,7]
    quick_sort(lst, 0, 5)
    assert lst == [5, 5, 5, 7, 7, 12]