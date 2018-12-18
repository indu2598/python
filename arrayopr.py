# # Python program to demonstrate
# # basic operations on single array
import numpy as np
 
# Defining Array 1
a = np.array([[1, 2],[3, 4]])
 
# Defining Array 2
b = np.array([(4, 3), (2, 1)])
               
# # Adding 1 to every element
# print ("Adding 1 to every element:\n", a + 1)
 
# # Subtracting 2 from each element
# print ("\nSubtracting 2 from each element:\n", b - 2)
 
# # sum of array elements Performing Unary operations
# print ("\nSum of all array elements:\n ", a.sum())
 
# # Adding two arrays Performing Binary operations
# print ("\nArray sum:\n", a + b)

#finding out the dimension of an array

print(f"the dimension of first aaray is {a.ndim} ")

print(f"the dimension of second  aaray is {b.ndim} ")

#finding out byte size of array element

print(f"the element size is {a.itemsize} ")

#finding out the type of element

print(f"data type of element is {a.dtype}")