name = input("Enter string with many duplicates:")
tem_var = " "
i = 0
while i < len(name):
    if name[i] != tem_var[len(tem_var)-1]:
        tem_var += name[i]
    i +=1
print(tem_var.strip())
