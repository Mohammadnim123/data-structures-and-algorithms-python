def insertion_sort(list_of_ints):
    """Sorts a list of integers 'in-place' from least to greatest"""
    
    for i in range(1, len(list_of_ints)): 
        j = (i - 1)
        int_to_insert = list_of_ints[i]

        while j >= 0 and int_to_insert < list_of_ints[j]:
            list_of_ints[j + 1] = list_of_ints[j]
            j -= 1
        list_of_ints[j + 1] = int_to_insert
    return list_of_ints



if __name__ == "__main__":
    print(insertion_sort([8,4,23,42,16,15]))
