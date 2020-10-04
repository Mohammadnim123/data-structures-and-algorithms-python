class Node():
    def __init__(self, value):
        """
        This class is to creat node with it value without link it to other node
        """
        self.value = value
        self.next = None


class LinkedList():
    """
    This class have the methods to insert , includes and __str__ to see output
    """
    def __init__(self):
        """
        make none value for the head of the linked list
        """
        self.head = None

    def __str__(self):
        """
        it print the linked list as string
        """
        current = self.head
        output = ''
        while current:
            output += "{ %s } -> " %current.value
            current = current.next
        output += "{ Null } -> "
        return output

    def ins_af(self,val,new):
      new_node = Node(new)
      curr = self.head
      while curr:
        if curr.value == val:
          temp = curr.next
          curr.next = new_node
          new_node.next = temp
        curr = curr.next

    def ins_bf(self,val,new):
      new_node = Node(new)
      curr = self.head
      while curr:
        if curr.next.value == val:
          temp = curr.next
          curr.next = new_node
          new_node.next = temp
          break
        curr = curr.next   


def kth(lls,k):
  length = 0
  if lls.head == None:
    raise ValueError('empty!!')
  curr = lls.head
  while curr.next:
    length +=1
    curr = curr.next
  val = length - k
  curr = lls.head
  for i in range(val):
    curr = curr.next
  return curr.value

def zip(lls1,lls2):
  if lls1.head == None:
    return None
  if lls2.head == None:
    return lls1
  curr1 = lls1.head
  curr2 = lls2.head

  while curr2 and curr1:
    temp1 = curr1.next
    temp2 = curr2.next
    curr1.next = curr2
    curr2.next = temp1
    curr1 = temp1
    curr2 = temp2
    if curr1.next == None:
      break
  if curr2:
    curr1.next = curr2
  return lls1

def rev(lls):
  p = None
  curr = lls.head
  n = curr.next
  while curr:
    curr.next = p
    p = curr
    curr = n
    if curr:
      n = curr.next
    else:
      break
  lls.head = p

def mid(lls):
  p1 = lls.head
  p2 = lls.head

  while p2.next:
    p1 = p1.next
    p2 = p2.next.next
    if p2 == None:
      break
  return p1

def palend(lls):
  val = mid(lls)
  lls2 = LinkedList()
  lls2.head = val
  rev(lls2)
  curr1 = lls.head
  curr2 = lls2.head
  while curr2:
    if curr1.value == curr2.value:
      curr1 = curr1.next
      curr2 = curr2.next
    else:
      return False
  return True




  

  


      




if __name__ == '__main__':
  # ll1 = LinkedList()
  # ll1.head = Node(1)
  # ll1.head.next = Node(3)
  # # ll1.head.next.next = Node(5)

  ll2 = LinkedList()
  ll2.head = Node(1)
  ll2.head.next = Node(2)
  ll2.head.next.next = Node(2)
  ll2.head.next.next.next = Node(1)
  # ll2.head.next.next.next.next = Node(1)
   
  # rev(ll2)

  

  print(mid(ll2).value)
  print(palend(ll2))