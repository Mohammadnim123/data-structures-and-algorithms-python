from data_structures_and_algorithms.data_structures.hashtable.hashtable import *

def split(strr): # to avoid using built-in methods
  output = ''
  splitted_arr = []
  for char in strr:
    if char == ',':
      continue
    if char == ' ':
      splitted_arr.append(output)
      output = ''
      continue
    output += char
  return splitted_arr

def repeated_word(strr):
    new_arr = split(strr)
    # print(new_arr)
    hashtable = Hashtable()
    for elem in new_arr:
        if hashtable.contains(elem.lower()):
            return elem.lower()
        hashtable.add(elem.lower(),1)

