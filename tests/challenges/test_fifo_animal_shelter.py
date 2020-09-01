from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import Dog, Cat, AnimalShelter

#######################################################
# Testing instantiation
#######################################################
def test_creating_empty_animal_shelter():
    assert AnimalShelter().front == None

def test_creating_dog_object():
    assert Dog().name == 'Ima dog'

def test_creating_cat_object():
    assert Cat().name == 'Ima cat'

#######################################################
# Testing Enqueue
#######################################################
def test_enqueue_one_to_animal_shelter():
    new_shelter = AnimalShelter()
    new_shelter.enqueue('dog')
    assert new_shelter.front.name == 'Ima dog'

def test_enqueue_many_to_animal_shelter():
    new_shelter = AnimalShelter()
    new_shelter.enqueue('dog')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('cat')
    assert new_shelter.front.name == 'Ima dog'   

#######################################################
# Testing dequeue
#######################################################
def test_dequeue_one_animal_from_shelter():
    new_shelter = AnimalShelter()
    new_shelter.enqueue('dog')
    assert new_shelter.dequeue('dog').name == 'Ima dog'
    assert new_shelter.front == None

def test_dequeue_dog_from_shelter_of_many():
    new_shelter = AnimalShelter()
    new_shelter.enqueue('dog')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('dog')
    assert new_shelter.dequeue('dog').name == 'Ima dog'

def test_dequeue_cat_from_shelter_of_many():
    new_shelter = AnimalShelter()
    new_shelter.enqueue('dog')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('dog')
    assert new_shelter.dequeue('cat').name == 'Ima cat'    

def test_dequeue_from_empty_shelter():
    new_shelter = AnimalShelter()
    assert new_shelter.dequeue('dog') == None

def test_dequeue_first_from_shelter_no_preference():
    new_shelter = AnimalShelter()
    new_shelter.enqueue('dog')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('cat')
    new_shelter.enqueue('dog')
    assert new_shelter.dequeue().name == 'Ima dog'
    assert new_shelter.front.name == 'Ima cat'  