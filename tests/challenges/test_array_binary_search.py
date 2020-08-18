from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import binary_search

def test_1():
    expected = 2
    actual = binary_search([4,8,15,16,23,42], 15)
    assert expected == actual

def test_2():
    expected = -1
    actual = binary_search([11,22,33,44,55,66,77], 90)
    assert expected == actual

def test_3():
    expected = 4
    actual = binary_search([11,22,33,44,55,66,77], 55)
    assert expected == actual

def test_4():
    expected = -1
    actual = binary_search([11,22,33,44,55,66,77], -1)
    assert expected == actual

def test_5():
    expected = -1
    actual = binary_search([11,22,33,44,55,66,77], 0)
    assert expected == actual


