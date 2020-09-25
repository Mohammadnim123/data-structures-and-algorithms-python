class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node


if __name__=='__main__':
    people = LinkedList()
    people.add('Nimrawi')
    people.add('Ghafri')
    people.add('Dana')
    people.add('Yazan')
    assert people.head.data == 'Nimrawi'
    assert people.head.next.data == 'Ghafri'
    assert people.head.next.next.data == 'Dana'
    assert people.head.next.next.next.data == 'Yazan'
    print('All test cases passed')