import numpy as nm 

import sys
import time

# s = range(1000) # list is created
# print(sys.getsizeof(4)*len(s))

# array1 = nm.arange(1000) # array is created with arange() in numpy
# print(array1.size* array1.itemsize)

###############################################
size = 100000
l1 = range(size)
l2 = range(size)

start = time.time()

result = [(x,y) for x, y in zip(l1,l2)]  # for loop with two elements
print((time.time()-start)*1000)

a1 = nm.arange(size)
a2 = nm.arange(size)
 
start = time.time()
result = a1+a2
print((time.time()-start)*1000)



###################################################
