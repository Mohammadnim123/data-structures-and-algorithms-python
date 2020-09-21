def merge_sort(arr):
    
    if len(arr) > 1:

        mid = len(arr)//2
        left = arr[:mid] 
        right = arr[mid:]

        merge_sort(left) 

        merge_sort(right)

        _merge(left, right, arr)
    return arr 


def _merge(left, right, lst):
    i, j, k = 0,0,0

    while i < len(left) and j < len(right): 

        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    if i == len(left): 

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    else: 
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1


if __name__ == "__main__":
    print(merge_sort([8,4,23,42,16,15]))