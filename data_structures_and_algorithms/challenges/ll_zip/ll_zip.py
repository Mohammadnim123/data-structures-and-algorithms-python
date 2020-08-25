from data_structures_and_algorithms.data_structures.linked_list.linked_list import Node,LinkedList

def zipLists(list1, list2):
    """
    takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1).
    """
    current1 = list1.head
    current2 = list2.head

    if not current1:
        list1.head = list2.head
        return list1.head

    if not current2:
        return list1.head

    temp = current2.next

    while current1.next and current2.next:
        current1.next, current2.next = current2, current1.next
        current1 = current2.next
        current2, temp = temp, temp.next

    if not current1.next:
        current1.next = current2
        return list1.head

    if not current2.next:
        current1.next, current2.next = current2, current1.next
        return list1.head

   


if __name__ == "__main__":
    first = LinkedList()
    second = LinkedList()

    first.append(1)
    first.append(2)
    first.append(3)
    first.append(4)
   
   
    second.append(5)
    second.append(6)
    
    

    print(first.__str__())
    print(second.__str__())
    zipLists(first,second)
    print(first.__str__())
    