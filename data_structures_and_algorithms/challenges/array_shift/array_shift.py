

def insertShiftArray(x,y):
  newList = []
  i=0
  while i<len(x):
  
    if x[i]<y and x[i+1]>y:
      newList.append(x[i]) 
      newList.append(y)
    else:
      newList.append(x[i])  
    i+=1
  return newList
