import numpy as np
arry1 = np.array([1,2,6,8,5,7])
arry2 = np.array([5,8,5,8,7,9])
print(arry1 * arry2)
age = input("enter age:")
age = int(age)
if 0<age<=3:
    print("free;")
elif 3<age<=10:
    print("pay 150")
elif 11<age<=60:
    print("pay 250")
else:
    print("pay 200")