from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack

class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.rear = 0
        

    def enqueue(self,*value):
        self.stack1.push(*value)
        self.rear = self.stack1.top.value

    def dequeue(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            return 'empty queue !!!'
        elif self.stack2.is_empty():
            while self.stack1.top:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

 

if __name__ == "__main__":
    neww = PseudoQueue()
  
    print (neww.dequeue())
    
    
  
    