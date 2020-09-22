def quick_sort(lst, left, right):
    if left < right:

        position = partition(lst, left, right)

        quick_sort(lst, left, position - 1)

        quick_sort(lst, position + 1, right)
    return lst

def partition(lst, left, right):
    pivot = lst[right]
    low = left - 1
    for i in range(left, right):
        if lst[i] <= pivot:
            low += 1
            swap(lst, i, low)

  
    swap(lst, right, low + 1)
    return low + 1

def swap(lst, i, low):
    lst[i], lst[low] = lst[low], lst[i]

if __name__ == "__main__":
   print(quick_sort([54,26,93,17,77,31,44,55,20], 0, 8)) 