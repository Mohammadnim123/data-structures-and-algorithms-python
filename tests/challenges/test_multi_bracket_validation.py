from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_1():
    expected = True
    actual = multi_bracket_validation('{}')
    assert expected == actual

def test_2():
    expected = True
    actual = multi_bracket_validation('{}(){}')
    assert expected == actual

def test_3():
    expected = True
    actual = multi_bracket_validation('()[[Extra Characters]]')
    assert expected == actual

def test_4():
    expected = True
    actual = multi_bracket_validation('(){}[[]]')
    assert expected == actual

def test_5():
    expected = True
    actual = multi_bracket_validation('{}{Code}[Fellows](())')
    assert expected == actual

def test_6():
    expected = False
    actual = multi_bracket_validation('[({}]')
    assert expected == actual

def test_7():
    expected = False
    actual = multi_bracket_validation('(](')
    assert expected == actual

def test_8():
    expected = False
    actual = multi_bracket_validation('{')
    assert expected == actual

def test_9():
    expected = False
    actual = multi_bracket_validation(')')
    assert expected == actual

def test_10():
    expected = False
    actual = multi_bracket_validation('[}')
    assert expected == actual





    