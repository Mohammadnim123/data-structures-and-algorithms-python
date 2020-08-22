class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None



    def insert(self,value):
        value !=None
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curent = self.head
            while curent.next:
                curent = curent.next
            curent.next = new_node

    def includes (self,value):
      if self.head==None:
          return False
      else:
          current=self.head
          while current:
              if current.value==value:
                  return True
              else :
                  current=current.next    
          return False             

    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += "{ %s } -> " %current.value
            current = current.next
        return output
        