# s = (1,4,78,83,86)
# for i in s:
#     print(f"\t {i}")

#sum using for loop

# num = input("enter any number:")
# total = 0

# for i in range(0,len(num)):
#     total += int(num[i])
# print(f"\n \t {total}")

#counting of different characters

name = input("enter your name:")
temp =" "
for i in range(0,len(name)):
    if name[i] not in temp:
        temp += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    