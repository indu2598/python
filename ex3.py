num = input("enter number containing more digits:")
length = len(num)
total = 0
i=0
while i<length:
    total += int(num[i])
    i +=1
print(f"total is : {total}")
