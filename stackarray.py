import numpy as np 
a1 = np.array([(2,4,6), (6,7,8)])
a2 = np.array([(4,6,7), (9,8,4)])
a3 = np.vstack(a1,a2)
a4 = np.hstack(a1,a2)

print(a3)

print(a4)