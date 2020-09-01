def multi_bracket_validation(input):
    my_values = []
    Round_op = input.count('(')
    Round_cl = input.count(')')
    Square_op = input.count('[')
    Square_cl = input.count(']')
    Curly_op = input.count('{')
    Curly_cl = input.count('}')

    Round_error = Round_op - Round_cl
    Square_error = Square_op - Square_cl
    Curly_error = Curly_op - Curly_cl

    if Round_error == 0:
        my_values.append(1)
    else:
        my_values.append(0)

    if Square_error == 0:
        my_values.append(1)
    else:
        my_values.append(0)

    if Curly_error == 0:
        my_values.append(1)
    else:
        my_values.append(0)


    
    if Round_error > 0:
        print("error unmatched opening ( remaining")
        
    elif Round_error < 0:
        print("error closing ) arrived without corresponding opening.")

    
    
    if Square_error > 0:
        print("error unmatched opening [ remaining")
        
    elif Square_error < 0:
        print("error closing ] arrived without corresponding opening.")

    
    if Curly_error > 0:
        print("error unmatched opening [ remaining")
        
    elif Curly_error < 0:
        print("error closing ] arrived without corresponding opening.")

    if my_values.__contains__(0):
        return False
    else:
        return True


if __name__ == "__main__":
    # multi_bracket_validation('{}')
    # multi_bracket_validation('{}(){}')
    # multi_bracket_validation('()[[Extra Characters]]')
    # multi_bracket_validation('(){}[[]]')
    # multi_bracket_validation('{}{Code}[Fellows](())	')


    # multi_bracket_validation('[({}]')
    # multi_bracket_validation('(](')
    # multi_bracket_validation('{')
    # multi_bracket_validation(')')
    multi_bracket_validation('[}')
   