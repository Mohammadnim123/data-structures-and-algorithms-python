from data_structures_and_algorithms.data_structures.hashtable.hashtable import *

def left_join(hash1,hash2):
    output = []
    single_elem = []
    for elem in hash1.map:
        if elem:
            current = elem.head
            
            while current:
                single_elem.append(current.data[0])
                single_elem.append(current.data[1])
                if hash2.contains(current.data[0]):
                    single_elem.append(hash2.get(current.data[0]))
                else:
                    single_elem.append(None)
                output.append(single_elem)
                single_elem = []
                current = current.next
    return output


if __name__ == "__main__":
    h1 = Hashtable()
    h1.add('fond','enamored')        
    h1.add('fnod', 'anger')          
    h1.add('fodn', 'employed')    
    h1.add('donf', 'garb')           
    h1.add('ofnd', 'usher')

    h2 = Hashtable()
    h2.add('fond', 'averse')
    h2.add('fnod', 'delight')
    h2.add('fodn', 'idle')
    h2.add('guide', 'follow')
    h2.add('flow', 'jam')


    print(left_join(h1,h2))