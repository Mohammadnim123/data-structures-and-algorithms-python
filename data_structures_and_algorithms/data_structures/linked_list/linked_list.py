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



    def insert(self,value):
        """
        add a vlaue for the first of the linked list
        """
        value !=None
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current=self.head
            self.head=new_node
            new_node.next=current




    def includes (self,value):
        """
        it search about specific value in the linked list
        """
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




    def append(self,value):
        """
        add a vlaue for the first of 
        """
        value !=None
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curent = self.head
            while curent.next:
                curent = curent.next
            curent.next = new_node



    def insertAfter(self, value, newVal):
        """
        in this method your value and any exist value then it will add your value after the choosen value
        """
        current = self.head
        print(current.next)
        while current is not None:
            if current.value == value:
                break
            current = current.next
        if current is None:
            print("Exception: the value not exisit in the linked list")
        else:
            new_node = Node(newVal)
            new_node.next = current.next
            current.next = new_node 

    
    
    def insertBefore(self, value, newVal):
        """
        in this method your value and any exist value then it will add your value before the choosen value
        """
        if self.head is None:
            print("List has no element")
            return

        if value == self.head.value:
            new_node = Node(newVal)
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        
        while current.next is not None:
            if current.next.value == value:
                break
            current = current.next
        if current.next is None:
            print("Exception: the value not exisit in the linked list")
        else:
            new_node = Node(newVal)
            new_node.next = current.next
            current.next = new_node  

 
    def kth_from_end(self, k):
        try:
            counter = -1
            current = self.head
            while current:
                current = current.next
                counter = counter + 1
            if counter >= k:
                current = self.head
                for i in range(counter - k):
                    current = current.next
            return current.value
        except:
            return "ValueError:your value not found"
   
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

    def insertbef(self,goal,newval):
        if self.head == None:
            self.head = Node(newval)
        else:
            curr = self.head
            while curr:
                if curr.next.value == goal:
                    temp = curr.next
                    newnode = Node(newval)
                    newnode.next = temp
                    curr.next = newnode
                    break
                curr = curr.next

    def kth(self, k):
        if self.head == None:
            raise ValueError('emty linkedlist')

        else:
            length = 0
            curr = self.head
            while curr:
                length += 1
                curr = curr.next
            new_length = length - k
            my_value = None
            curr = self.head
            for i in range(new_length):
                my_value = curr.value
                curr = curr.next
            if my_value == None:
                raise Exception("out of the range")
            return my_value


    def rev(self):
        curr = self.head
        p = None
        n = curr.next
        while n:
            curr.next = p
            p = curr
            curr = n
            n = n.next
            curr.next = p
            self.head = curr

    def mid(self):
        p1 = self.head
        p2 = self.head
        
        while p2 and p2.next :
            p1 = p1.next
            p2 = p2.next.next
        return p1

    def palindrom(self):
        length = 0
        curr = self.head
        while curr:
            length+=1
            curr = curr.next
        new = LinkedList()
        mid = self.mid()
        if length % 2 == 1:
            new.head = mid.next
        if length % 2 == 0:
            new.head = mid
        new.rev()
        
        curr1 = self.head
        curr2 = new.head
        while curr2:
            if curr1.value != curr2.value:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        return True



if __name__ == "__main__":
    llist = LinkedList() 
  
    # Use push() to construct below list 
    # 1->12->1->4->1 
    llist.append('a') 
    llist.append('bc') 
    llist.append('d') 
    llist.append('bc') 
    llist.append('a') 
 

    
    
    
    print(llist.palindrom())
    # print(llist)

                 

            

   
   
    
    
    
    


        