name = input("enter you name :")
name = name.strip()
length = len(name)
tem_var = ''
i = 0
while i < length:
    if name[i] not in tem_var:
        tem_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i +=1