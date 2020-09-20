import pytest
from data_structures_and_algorithms.challenges.Insertion_Sort.Insertion_Sort import insertion_sort

def test_empty_list():
    lst = []
    insertion_sort(lst)
    assert lst == []

def test_insertion_sort():
    lst = [8,4,23,42,16,15]
    insertion_sort(lst)
    assert lst == [4,8,15,16,23,42]

def test_reverse_sorted():
    lst = [20,18,12,8,5,-2]
    insertion_sort(lst)
    assert lst == [-2,5,8,12,18,20]

def test_few_uniques_sort():
    lst = [5,12,7,5,5,7]
    insertion_sort(lst)
    assert lst == [5,5,5,7,7,12]

def test_nearly_sorted():
    lst = [2,3,5,7,13,11]
    insertion_sort(lst)
    assert lst == [2,3,5,7,11,13]

def test_non_integers_sort():
    lst = ['a', 's', 'd', 'f', 'g', 'A']
    insertion_sort(lst)
    assert lst == ['A', 'a', 'd', 'f', 'g', 's']