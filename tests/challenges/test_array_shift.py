from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray

def test_1():
    expected = [2,4,5,6,8]
    actual = insertShiftArray([2,4,6,8], 5)
    assert expected == actual

def test_2():
    expected = [4,8,15,16,23,42]
    actual = insertShiftArray([4,8,15,23,42], 16)
    assert expected == actual

