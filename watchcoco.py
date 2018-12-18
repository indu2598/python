name , age = input("Enter name and age comma seprated:").split(",")
age = age.strip() #strip() method is a string method that's why use this before converting to int.
age = int(age)
name = name.strip()
# age = age.strip()
if (name[0]=='a' or name[0]=='A') and age >= 10:
    print("you can watch coco movie")
else:
    print("you can't watch coco movie")