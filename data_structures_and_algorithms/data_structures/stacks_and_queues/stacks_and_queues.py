class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, *value):
        """
        it takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
        """
        
        for i in value:
            node = Node(i)
            # Special case: if empty queue
            # f -> 1 <- r
            if not self.front and not self.rear:
                self.front = node
                self.rear = node

            
            else:
                old_rear = self.rear
                self.rear = node
                old_rear.next = self.rear
                # front -> 1 -> 2 -> 3 <- rear


    def dequeue(self):
        """
        it removes the node from the front of the queue, and returns the node’s value.
        """

        try:
            self.front.value
        except AttributeError:
            return "empty queue"
        else:
            temp = self.front
            tempp = temp.next
            self.front = tempp
            return temp.value

    def peek(self):
        """
        returns the value of the node located in the front of the queue, without removing it from the queue.
        """
        try:
            return self.front.value
        except AttributeError as e:
            return f"Empty Queue!!!"
        except Exception as e:
            return f"Some other exception happened!!! "

    def is_empty(self):
        """
        returns a boolean indicating whether or not the queue is empty.
        """
        if self.front:
            return False
        else:
            return True



class Stack:
    def __init__(self):
        self.max = 10000
        self.top = None

    def push(self, *value):
        """
        it takes any values as an argument and adds a new node with that values to the top of the stack with an O(1) Time performance.p
        """
        for i in value:
            node = Node(i)
            temp = self.top 
            self.top = node 
            self.top.next = temp 

    def pop(self):
        '''
        it removes the node from the top of the stack, and returns the node’s value.
        '''
        try:
           
            result = self.top.value
            temp = self.top.next
            self.top = temp
            return result
        except AttributeError:
            return "this is empty stack"
        


    def peek(self):
        """
        it returns the value of the node located on top of the stack, without removing it from the stack.
        """
        try:
            return self.top.value
        except AttributeError as e:
            return "Stack is empty"

    def is_empty(self):
        '''
        it returns a boolean indicating whether or not the stack is empty.n
        '''
        if self.top:
            return False
        else:
            return True

# pushing 3
# top -> 4 -> 5 -> None


if __name__ == '__main__':
    # eaters = Queue()
    # # print(eaters.peek())
    # eaters.enqueue("Saed","Ahmad")
    
    # # print(eaters.dequeue()) # should return Saed
    # print(eaters.front.value) # Saed
    # print(eaters.rear.value) # Ahmad
    # print(eaters.peek()) # Saed
    
    
    fruits = Stack()
    fruits.push('me9ba7','mhawesh')
   
    print(fruits.pop())