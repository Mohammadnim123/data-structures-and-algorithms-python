from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import *

##########################################################################################
                                    #Stack tests
###########################################################################################

def test_push_onto_a_stack():
    value = Stack()
    value.push('hello')
    expected = 'hello'
    actual = value.top.value
    assert expected == actual

def test_push_multiple_values_onto_a_stack():
    value = Stack()
    value.push('hello','world')
    expected = 'world'
    actual = value.top.value
    assert expected == actual

def test_pop_off_the_stack():
    value = Stack()
    value.push('hello','world')
    expected = 'world'
    actual = value.pop()
    assert expected == actual

def test_empty_a_stack_after_multiple_pops():
    value = Stack()
    value.push('hello','world')
    value.pop()
    value.pop()
    expected = True
    actual = value.is_empty()
    assert expected == actual

def test_peek_the_next_item_on_the_stack():
    value = Stack()
    value.push('hello','world')
    expected = 'world'
    actual = value.peek()
    assert expected == actual

def test_instantiate_an_empty_stack():
    value = Stack()
    expected = "Stack is empty"
    actual = value.peek()
    assert expected == actual



def test_pop_on_empty_stack_raises_exception():
    value = Stack()
    expected = "this is empty stack"
    actual = value.pop()
    assert expected == actual


##########################################################################################
                                    #Queues tests
###########################################################################################




def test_enqueue_into_a_queue():
    value = Queue()
    value.enqueue('hello')
    expected = 'hello'
    actual = value.rear.value
    assert expected == actual


def test_mulyple_enqueue_into_a_queue():
    value = Queue()
    value.enqueue('hello','world')
    expected = 'world'
    actual = value.rear.value
    assert expected == actual

def test_dequeue_out_of_a_queue_the_expected_value():
    value = Queue()
    value.enqueue('hello','world')
    expected = 'hello'
    actual = value.dequeue()
    assert expected == actual

def test_peek_into_a_queue_seeing_the_expected_value():
    value = Queue()
    value.enqueue('hello','world')
    expected = 'hello'
    actual = value.peek()
    assert expected == actual

def test_empty_a_queue_after_multiple_dequeues():
    value = Queue()
    value.enqueue('hello','world')
    value.dequeue()
    value.dequeue()
    expected = 'Empty Queue!!!'
    actual = value.peek()
    assert expected == actual

def test_instantiate_an_empty_queue():
    value = Queue()
    expected = 'Empty Queue!!!'
    actual = value.peek()
    assert expected == actual

def test_dequeue_on_empty_queue_raises_exception():

    value = Queue()
    expected = "empty queue"
    actual = value.dequeue()
    assert expected == actual










