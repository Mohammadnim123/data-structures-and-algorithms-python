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
        