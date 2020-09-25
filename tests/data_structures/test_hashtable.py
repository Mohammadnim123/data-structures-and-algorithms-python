from data_structures_and_algorithms.data_structures.hashtable.hashtable import Hashtable

def test_add_key_value():
    table = Hashtable()
    table.add('Mohammad','Mansaf')
    assert table.map[table.hash('Mohammad')].head.data == ['Mohammad','Mansaf']

def test_update_key_value():
    table = Hashtable()
    table.add('Mohammad','Mansaf')
    table.add('Mohammad','Maglobah')
    assert table.map[table.hash('Mohammad')].head.data[1] == 'Maglobah'


def test_get_value_from_key():
    table = Hashtable()
    table.add('Mohammad','Mansaf')
    assert table.get('Mohammad') == 'Mansaf'

def test_get_value_not_in_table():
    table = Hashtable()
    assert table.get('Mohammad') == 'this key not found'

def test_handle_collision():
    table = Hashtable()
    table.add('Mohammad','Mansaf')
    table.add('Mmmohaad','Maglobah')
    assert table.map[table.hash('Mohammad')].head.data == ['Mohammad','Mansaf']
    assert table.map[table.hash('Mohammad')].head.next.data == ['Mmmohaad','Maglobah']
    


def test_retrieve_data_with_collision():
    table = Hashtable()
    table.add('Mohammad','Mansaf')
    table.add('Mmmohaad','Maglobah')
    assert table.get('Mohammad') == 'Mansaf'
    assert table.get('Mmmohaad') == 'Maglobah'


