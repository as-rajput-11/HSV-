from re import L
import numpy as np
from PIL import Image
from numpy import asarray

img = Image.open("1.jpg")
m = np.array(img) 
l1 = m
def transpose(l1, l2):

 # iterate over list l1 to the length of an item
 for i in range(len(l1[1])):
  # print(i)
  row =[]
  for item in l1:
   # appending to new list with values and index positions
   # i contains index position and item contains values
   row.append(item[i])
  l2.append(row)
 return l2

# Driver code

l2 = []
transpose(l1, l2)    
l2.reverse()
im = Image.fromarray(np.uint8(l2)).convert('RGB')
im.save("v6.png")
